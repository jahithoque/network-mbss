# MBSS pages as Markdown

One file per Confluence page. Create them in this order, with these titles:

| # | File | Confluence page title | Parent page | Labels |
|---|---|---|---|---|
| 1 | [00-overview.md](00-overview.md) | Network MBSS | (top level) | `mbss` |
| 2 | [01-checkpoint.md](01-checkpoint.md) | MBSS – Firewall – Check Point | Network MBSS | `mbss, mbss-platform` |
| 3 | [02-bluecoat.md](02-bluecoat.md) | MBSS – Proxy – BlueCoat ProxySG | Network MBSS | `mbss, mbss-platform` |
| 4 | [03-f5.md](03-f5.md) | MBSS – Load Balancer – F5 BIG-IP | Network MBSS | `mbss, mbss-platform` |
| 5 | [04-cisco-ios.md](04-cisco-ios.md) | MBSS – Routers & Switches – Cisco IOS | Network MBSS | `mbss, mbss-platform` |
| 6 | [05-exceptions.md](05-exceptions.md) | MBSS – Exceptions & Waivers Register | Network MBSS | `mbss, mbss-exceptions` |
| 7 | [06-automation-backlog.md](06-automation-backlog.md) | MBSS – Automation Backlog | Network MBSS | `mbss, mbss-automation` |

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
