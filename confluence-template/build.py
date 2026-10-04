"""Render the MBSS pages in pages.py to three paste-ready formats.

  output/storage/<slug>.xml  Confluence storage format (source editor / REST API)
  output/wiki/<slug>.txt     Confluence wiki markup (Insert > Markup)
  mbss-confluence-kit.html   Preview page with copy buttons for all formats

Run: python3 build.py
"""

import html
import json
import pathlib

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
    return "\n".join(out)


# ------------------------------------------------------------ wiki markup

def w_esc(s):
    for ch in "[]{}|":
        s = s.replace(ch, "\\" + ch)
    return s


def w_inline(x):
    out = ""
    for i in as_inlines(x):
        if isinstance(i, str):
            out += w_esc(i)
        elif i[0] == "b":
            out += f"*{w_esc(i[1])}*"
        elif i[0] == "i":
            out += f"_{w_esc(i[1])}_"
        elif i[0] == "code":
            out += "{{" + w_esc(i[1]) + "}}"
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
    return "\n\n".join(out)


# ------------------------------------------------------------ HTML (preview + rich copy)

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
            out += f'<span class="cf-st cf-st-{i[1].lower()}">{h_esc(i[2])}</span>'
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


def h_blocks(blocks):
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
            out.append(f'<div class="cf-panel cf-panel-{b[1]}"><p><strong>{h_esc(b[2])}</strong></p>{h_blocks(b[3])}</div>')
        elif t == "toc":
            out.append('<p class="cf-macro">[Insert Table of Contents macro here]</p>')
        elif t == "props":
            out.append('<p class="cf-macro">[Page Properties macro: put the table below inside it]</p>'
                       + h_table(None, b[2], header_col=True, cls="cf-props"))
        elif t == "report":
            out.append(f'<p class="cf-macro">[Insert Page Properties Report macro here. CQL: {h_esc(b[1])}]</p>')
        elif t == "table":
            wide = "cf-wide" if len(b[1]) > 8 else ""
            out.append(h_table(b[1], b[2], cls=wide))
        elif t == "expand":
            out.append(f'<details class="cf-expand" open><summary>{h_esc(b[1])}</summary>{h_blocks(b[2])}</details>')
        elif t == "code":
            out.append(f'<pre class="cf-code"><code>{h_esc(b[1])}</code></pre>')
    return "\n".join(out)


# ------------------------------------------------------------ main

def main():
    pages = all_pages()
    (HERE / "output/storage").mkdir(parents=True, exist_ok=True)
    (HERE / "output/wiki").mkdir(parents=True, exist_ok=True)
    kit = []
    for pg in pages:
        storage = s_blocks(pg["blocks"])
        wiki = w_blocks(pg["blocks"])
        (HERE / f"output/storage/{pg['slug']}.xml").write_text(storage + "\n", encoding="utf-8")
        (HERE / f"output/wiki/{pg['slug']}.txt").write_text(wiki + "\n", encoding="utf-8")
        kit.append({k: pg[k] for k in ("slug", "title", "tab", "parent", "label")}
                   | {"html": h_blocks(pg["blocks"]), "wiki": wiki, "storage": storage})

    data = json.dumps(kit, ensure_ascii=False).replace("</", "<\\/")
    template = (HERE / "kit_template.html").read_text(encoding="utf-8")
    (HERE / "mbss-confluence-kit.html").write_text(template.replace("__KIT_DATA__", data), encoding="utf-8")
    print(f"Built {len(pages)} pages")


if __name__ == "__main__":
    main()
