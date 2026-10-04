# Network MBSS – Confluence templates

Templates for the MBSS pages covering Check Point, BlueCoat ProxySG, F5 BIG-IP and Cisco IOS.

| Page | Purpose |
|---|---|
| Network MBSS (parent) | Document control, scope, legends, coverage dashboard, cross-vendor matrix, Rule ID convention, review process |
| MBSS – Firewall – Check Point | Rule register + rule details + automation limitations |
| MBSS – Proxy – BlueCoat ProxySG | 〃 |
| MBSS – Load Balancer – F5 BIG-IP | 〃 |
| MBSS – Routers & Switches – Cisco IOS | 〃 |
| MBSS – Exceptions & Waivers Register | Approved deviations with expiry dates |
| MBSS – Automation Backlog | Rules that are PARTIAL, MANUAL or PLANNED |

Rule register columns: Rule ID · Rule Name · Domain · Description / Requirement · Severity ·
Expected (Compliant) Value · Current Check (Automation Tool) · Old Check · Automation Status ·
Last Review (Date / By) · Comments.

## Files

- `mbss-confluence-kit.html`: open in a browser, pick a page, press **Copy page**, then in Confluence Data Center press Ctrl+Shift+D (Insert › Markup) in the page body and paste. A Cloud copy and the storage format are there too.
- `output/network-mbss-confluence.md`: all pages in one Markdown file, with page titles and how to paste on Windows at the top
- `output/wiki/*.txt`: Confluence wiki markup (Insert › Markup › Confluence wiki)
- `output/storage/*.xml`: Confluence storage format (source editor or REST API `body.storage`)
- `pages.py`: page content (edit here)
- `build.py`: renders `pages.py` into all three formats. Run `python3 build.py` after editing.
