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

- `mbss-confluence-kit.html`: preview of every page, with copy buttons for each format
- `output/wiki/*.txt`: Confluence wiki markup (Insert › Markup › Confluence wiki)
- `output/storage/*.xml`: Confluence storage format (source editor or REST API `body.storage`)
- `pages.py`: page content (edit here)
- `build.py`: renders `pages.py` into all three formats. Run `python3 build.py` after editing.
