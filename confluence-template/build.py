"""Render the MBSS pages in pages.py to three paste-ready formats.

  output/storage/<slug>.xml  Confluence storage format (source editor / REST API)
  output/wiki/<slug>.txt     Confluence wiki markup (Insert > Markup)
  output/markdown/<slug>.md  Markdown (open on GitHub, copy the rendered page, paste)
  mbss-confluence-kit.html   Preview page with copy buttons for all formats

Run: python3 build.py
"""

import html
import json
import pathlib
import re

from pages import all_pages

HERE = pathlib.Path(__file__).parent


def as_inlines(x):
    return [x] if isinstance(x, (str, tuple)) else x


# ------------------------------------------------------------ storage format

def s_esc(s):
    return html.escape(s, quote=False)


def s_macro(name, params=None, body=None, plain=None):
    out = f'<ac:structured-macro ac:name="{name}">'
    for k, v in (params or {}).items():
        out += f'<ac:parameter ac:name="{k}">{s_esc(v)}</ac:parameter>'
    if body is not None:
        out += f"<ac:rich-text-body>{body}</ac:rich-text-body>"
    if plain is not None:
        out += f"<ac:plain-text-body><![CDATA[{plain.replace(']]>', ']]]]><![CDATA[>')}]]></ac:plain-text-body>"
    return out + "</ac:structured-macro>"


def s_inline(x):
    out = ""
    for i in as_inlines(x):
        if isinstance(i, str):
            out += s_esc(i)
        elif i[0] == "b":
            out += f"<strong>{s_esc(i[1])}</strong>"
        elif i[0] == "i":
            out += f"<em>{s_esc(i[1])}</em>"
        elif i[0] == "code":
            out += f"<code>{s_esc(i[1])}</code>"
        elif i[0] == "st":
            out += s_macro("status", {"colour": i[1], "title": i[2]})
        elif i[0] == "ph":
            out += f"<em>[{s_esc(i[1])}]</em>"
        elif i[0] == "br":
            out += "<br />"
    return out


def s_table(headers, rows, header_col=False):
    out = "<table><tbody>"
    if headers:
        out += "<tr>" + "".join(f"<th><p>{s_inline(h)}</p></th>" for h in headers) + "</tr>"
    for row in rows:
        out += "<tr>"
        for n, cell in enumerate(row):
            tag = "th" if header_col and n == 0 else "td"
            out += f"<{tag}><p>{s_inline(cell)}</p></{tag}>"
        out += "</tr>"
    return out + "</tbody></table>"


def s_blocks(blocks):
    out = []
    for b in blocks:
        t = b[0]
        if t == "h":
            out.append(f"<h{b[1]}>{s_esc(b[2])}</h{b[1]}>")
        elif t == "p":
            out.append(f"<p>{s_inline(b[1])}</p>")
        elif t == "ul":
            out.append("<ul>" + "".join(f"<li>{s_inline(i)}</li>" for i in b[1]) + "</ul>")
        elif t == "panel":
            out.append(s_macro(b[1], {"title": b[2]}, s_blocks(b[3])))
        elif t == "toc":
            out.append(s_macro("toc", {"maxLevel": str(b[1])}))
        elif t == "props":
            out.append(s_macro("details", {"id": b[1]}, s_table(None, b[2], header_col=True)))
        elif t == "report":
            out.append(s_macro("detailssummary", {"cql": b[1], "headings": b[2]}))
        elif t == "table":
            out.append(s_table(b[1], b[2]))
        elif t == "expand":
            out.append(s_macro("expand", {"title": b[1]}, s_blocks(b[2])))
        elif t == "code":
            out.append(s_macro("code", plain=b[1]))
        elif t == "alt":
            out.append(s_blocks(b[1]))
    return "\n".join(out)


# ------------------------------------------------------------ wiki markup

# Text the wiki renderer would turn into an emoticon, e.g. "15.2(x)" -> red cross.
W_EMOTICON = re.compile(r"\((x|i|/|!|\?|y|n|on|off|\*[rgby]?|-|\+)\)|[:;]-?[()PDp]")


def w_esc(s):
    for ch in "[]{}|":
        s = s.replace(ch, "\\" + ch)
    return W_EMOTICON.sub(lambda m: "\\" + m.group(0), s)


def w_wrap(open_, text, close):
    # *bold *, _italic _ etc. don't render if the marker sits next to a space,
    # so keep leading/trailing spaces outside the markers.
    core = text.strip()
    lead = text[:len(text) - len(text.lstrip())]
    trail = text[len(text.rstrip()):]
    return lead + open_ + core + close + trail if core else text


def w_inline(x):
    out = ""
    for i in as_inlines(x):
        if isinstance(i, str):
            out += w_esc(i)
        elif i[0] == "b":
            out += w_wrap("*", w_esc(i[1]), "*")
        elif i[0] == "i":
            out += w_wrap("_", w_esc(i[1]), "_")
        elif i[0] == "code":
            out += w_wrap("{{", w_esc(i[1]), "}}")
        elif i[0] == "st":
            out += "{status:colour=%s|title=%s}" % (i[1], i[2])
        elif i[0] == "ph":
            out += f"_\\[{w_esc(i[1])}\\]_"
        elif i[0] == "br":
            out += " \\\\ "
    return out or " "


def w_table(headers, rows, header_col=False):
    lines = []
    if headers:
        lines.append("||" + "||".join(w_inline(h) for h in headers) + "||")
    for row in rows:
        if header_col:
            lines.append("||" + w_inline(row[0]) + "|" + "|".join(w_inline(c) for c in row[1:]) + "|")
        else:
            lines.append("|" + "|".join(w_inline(c) for c in row) + "|")
    return "\n".join(lines)


def w_blocks(blocks):
    out = []
    for b in blocks:
        t = b[0]
        if t == "h":
            out.append(f"h{b[1]}. {b[2]}")
        elif t == "p":
            out.append(w_inline(b[1]))
        elif t == "ul":
            out.append("\n".join("* " + w_inline(i) for i in b[1]))
        elif t == "panel":
            out.append("{%s:title=%s}\n%s\n{%s}" % (b[1], b[2], w_blocks(b[3]), b[1]))
        elif t == "toc":
            out.append("{toc:maxLevel=%d}" % b[1])
        elif t == "props":
            out.append("{details:id=%s}\n%s\n{details}" % (b[1], w_table(None, b[2], header_col=True)))
        elif t == "report":
            out.append("{detailssummary:cql=%s|headings=%s}" % (b[1], b[2]))
        elif t == "table":
            out.append(w_table(b[1], b[2]))
        elif t == "expand":
            out.append("{expand:title=%s}\n%s\n{expand}" % (b[1], w_blocks(b[2])))
        elif t == "code":
            out.append("{code}\n%s\n{code}" % b[1])
        elif t == "alt":
            out.append(w_blocks(b[1]))
    return "\n\n".join(out)


# ------------------------------------------------------------ HTML (preview + Cloud copy)
#
# mode="preview": the kit's preview of the wiki / storage version, with macros
# drawn as labelled boxes.
# mode="cloud": what "Copy for Confluence Cloud" puts on the clipboard. Status
# lozenges, panels and expands carry the data attributes the Cloud editor's
# paste parser (@atlaskit/adf-schema parseDOM rules) turns back into real
# elements. Macros that can't be pasted (TOC, Page Properties, the report) are
# left out or replaced by plain tables, so a pasted page needs no follow-up.

ADF_COLOUR = {"Grey": "neutral", "Red": "red", "Yellow": "yellow",
              "Green": "green", "Blue": "blue", "Purple": "purple"}


def h_esc(s):
    return html.escape(s, quote=True)


def h_inline(x):
    out = ""
    for i in as_inlines(x):
        if isinstance(i, str):
            out += h_esc(i)
        elif i[0] == "b":
            out += f"<strong>{h_esc(i[1])}</strong>"
        elif i[0] == "i":
            out += f"<em>{h_esc(i[1])}</em>"
        elif i[0] == "code":
            out += f"<code>{h_esc(i[1])}</code>"
        elif i[0] == "st":
            out += (f'<span class="cf-st cf-st-{i[1].lower()}" data-node-type="status" '
                    f'data-color="{ADF_COLOUR[i[1]]}" data-style="" data-text="{h_esc(i[2])}">{h_esc(i[2])}</span>')
        elif i[0] == "ph":
            out += f'<em class="cf-ph">[{h_esc(i[1])}]</em>'
        elif i[0] == "br":
            out += "<br>"
    return out


def h_table(headers, rows, header_col=False, cls=""):
    out = f'<div class="cf-tw"><table class="cf-table {cls}"><tbody>'
    if headers:
        out += "<tr>" + "".join(f"<th>{h_inline(h)}</th>" for h in headers) + "</tr>"
    for row in rows:
        out += "<tr>"
        for n, cell in enumerate(row):
            tag = "th" if header_col and n == 0 else "td"
            out += f"<{tag}>{h_inline(cell)}</{tag}>"
        out += "</tr>"
    return out + "</tbody></table></div>"


def h_blocks(blocks, mode):
    preview = mode == "preview"
    out = []
    for b in blocks:
        t = b[0]
        if t == "h":
            out.append(f"<h{b[1]}>{h_esc(b[2])}</h{b[1]}>")
        elif t == "p":
            out.append(f"<p>{h_inline(b[1])}</p>")
        elif t == "ul":
            out.append("<ul>" + "".join(f"<li>{h_inline(i)}</li>" for i in b[1]) + "</ul>")
        elif t == "panel":
            out.append(f'<div class="cf-panel cf-panel-{b[1]}" data-panel-type="{b[1]}">'
                       f'<p><strong>{h_esc(b[2])}</strong></p>{h_blocks(b[3], mode)}</div>')
        elif t == "toc" and preview:
            out.append('<p class="cf-macro">Table of contents</p>')
        elif t == "props":
            table = h_table(None, b[2], header_col=True, cls="cf-props")
            out.append(f'<div class="cf-macrobox"><p class="cf-macrolabel">Page Properties</p>{table}</div>'
                       if preview else table)
        elif t == "report" and preview:
            out.append(f'<p class="cf-macro">Page Properties Report: one row per page where {h_esc(b[1])}</p>')
        elif t == "table":
            wide = "cf-wide" if len(b[1]) > 8 else ""
            out.append(h_table(b[1], b[2], cls=wide))
        elif t == "expand":
            out.append(f'<div class="cf-expand" data-node-type="expand" data-title="{h_esc(b[1])}">{h_blocks(b[2], mode)}</div>')
        elif t == "code":
            out.append(f'<pre class="cf-code"><code>{h_esc(b[1])}</code></pre>')
        elif t == "alt":
            out.append(h_blocks(b[1] if preview else b[2], mode))
    return "\n".join(out)


# ------------------------------------------------------------ Markdown
#
# Same choices as the Cloud copy: no TOC, Page Properties as a plain table, the
# hand-updated coverage table instead of the report. Status values become plain
# text, panels become quotes and expands become ### sections.

M_SPECIAL = re.compile(r"([\\`*_\[\]<>|])")


def m_esc(s):
    return M_SPECIAL.sub(r"\\\1", s)


def m_inline(x):
    out = ""
    for i in as_inlines(x):
        if isinstance(i, str):
            out += m_esc(i)
        elif i[0] == "b":
            out += w_wrap("**", m_esc(i[1]), "**")
        elif i[0] == "i":
            out += w_wrap("*", m_esc(i[1]), "*")
        elif i[0] == "code":
            out += "`" + i[1].replace("|", "\\|") + "`"
        elif i[0] == "st":
            out += i[2]
        elif i[0] == "ph":
            out += f"*\\[{m_esc(i[1])}\\]*"
        elif i[0] == "br":
            out += " — "
    return out.strip() or " "


def m_table(headers, rows, header_col=False):
    if not headers:
        headers = ["Property", "Value"]
    lines = ["| " + " | ".join(m_inline(h) for h in headers) + " |",
             "|" + "|".join("---" for _ in headers) + "|"]
    for row in rows:
        cells = [m_inline(c) for c in row]
        if header_col:
            cells[0] = f"**{cells[0]}**"
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def m_blocks(blocks):
    out = []
    for b in blocks:
        t = b[0]
        if t == "h":
            out.append("#" * b[1] + " " + b[2])
        elif t == "p":
            out.append(m_inline(b[1]))
        elif t == "ul":
            out.append("\n".join("- " + m_inline(i) for i in b[1]))
        elif t == "panel":
            body = f"**{m_esc(b[2])}**\n\n" + m_blocks(b[3])
            out.append("\n".join(("> " + line).rstrip() for line in body.split("\n")))
        elif t == "props":
            out.append(m_table(None, b[2], header_col=True))
        elif t == "table":
            out.append(m_table(b[1], b[2]))
        elif t == "expand":
            out.append("### " + b[1] + "\n\n" + m_blocks(b[2]))
        elif t == "code":
            out.append("```\n" + b[1] + "\n```")
        elif t == "alt":
            out.append(m_blocks(b[2]))
    return "\n\n".join(out)


MD_INDEX_HEAD = """# MBSS pages as Markdown

One file per Confluence page. Create them in this order, with these titles:

| # | File | Confluence page title | Parent page | Labels |
|---|---|---|---|---|
"""

MD_INDEX_TAIL = """

## Pasting into Confluence Data Center (Windows)

**Recommended: copy the formatted page from GitHub**

1. Open the page's `.md` file on GitHub. It shows formatted, with real tables.
2. Click inside the formatted text, press `Ctrl+A` to select it, then `Ctrl+C` to copy.
3. In Confluence, create the page, type the title from the table above, click in the body and press `Ctrl+V`.

Headings, tables, lists, bold text and code paste as normal Confluence formatting.

**Alternative: Insert › Markup › Markdown**

Open the file in Notepad, `Ctrl+A`, `Ctrl+C`. In the Confluence editor press `Ctrl+Shift+D`, choose **Markdown**, paste, and check the preview before pressing Insert. Confluence Data Center doesn't always turn Markdown tables into real tables, so if the preview shows jumbled text, use the GitHub route instead.

## What Markdown can't carry

Markdown has no Confluence macros, so these pages use plain equivalents:

- Severity and automation status (HIGH, AUTOMATED, …) are plain text. To get coloured lozenges, type `/status` in a cell or use the `output/wiki` files.
- "How to maintain this page" is a quote block instead of an info panel.
- Rule details is a normal section instead of an expand.
- The summary at the top of each platform page is a plain table, and the overview's coverage dashboard is a table you update by hand. The `output/wiki` files keep the Page Properties macros and the self-updating report.

Don't edit these files by hand. They are regenerated from `pages.py` by `python3 confluence-template/build.py`.
"""


def m_index(pages):
    rows = [
        f"| {n} | [{p['slug']}.md]({p['slug']}.md) | {p['title']} | {p['parent'] or '(top level)'} | `{p['label']}` |"
        for n, p in enumerate(pages, 1)
    ]
    return MD_INDEX_HEAD + "\n".join(rows) + MD_INDEX_TAIL


# ------------------------------------------------------------ main

def main():
    pages = all_pages()
    (HERE / "output/storage").mkdir(parents=True, exist_ok=True)
    (HERE / "output/wiki").mkdir(parents=True, exist_ok=True)
    (HERE / "output/markdown").mkdir(parents=True, exist_ok=True)
    kit = []
    for pg in pages:
        storage = s_blocks(pg["blocks"])
        wiki = w_blocks(pg["blocks"])
        (HERE / f"output/storage/{pg['slug']}.xml").write_text(storage + "\n", encoding="utf-8")
        (HERE / f"output/wiki/{pg['slug']}.txt").write_text(wiki + "\n", encoding="utf-8")
        (HERE / f"output/markdown/{pg['slug']}.md").write_text(m_blocks(pg["blocks"]) + "\n", encoding="utf-8")
        kit.append({k: pg[k] for k in ("slug", "title", "tab", "parent", "label")}
                   | {"preview": h_blocks(pg["blocks"], "preview"), "cloud": h_blocks(pg["blocks"], "cloud"),
                      "wiki": wiki, "storage": storage})

    (HERE / "output/markdown/README.md").write_text(m_index(pages), encoding="utf-8")
    data = json.dumps(kit, ensure_ascii=False).replace("</", "<\\/")
    template = (HERE / "kit_template.html").read_text(encoding="utf-8")
    (HERE / "mbss-confluence-kit.html").write_text(template.replace("__KIT_DATA__", data), encoding="utf-8")
    print(f"Built {len(pages)} pages")


if __name__ == "__main__":
    main()
