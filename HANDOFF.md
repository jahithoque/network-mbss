# Network MBSS Confluence pages – handoff

Summary of the Claude Code (web) session that produced `confluence-template/`, so the work can continue in Claude Code desktop.

## Goal

Build a Confluence page set holding the MBSS (Minimum Baseline Security Standard) documents for four platforms:

| Platform | Vendor / product | Rule ID prefix |
|---|---|---|
| Firewall | Check Point (Gaia OS, gateways + management) | `CP` |
| Proxy | Symantec BlueCoat ProxySG (SGOS) | `BC` |
| Load balancer | F5 BIG-IP (TMOS) | `F5` |
| Routers & switches | Cisco IOS / IOS-XE | `CSCO` |

Each rule has to show its name, description, the **current check in the Network Automation tool**, the **old check**, the **last review**, and comments. The user pastes the real rules in themselves.

## What was decided

1. **Page tree:** one parent page with six child pages. One long page holding four 100+ row tables gets slow to edit.
   ```
   Network MBSS                                (parent: overview + dashboard)
   ├── MBSS – Firewall – Check Point
   ├── MBSS – Proxy – BlueCoat ProxySG
   ├── MBSS – Load Balancer – F5 BIG-IP
   ├── MBSS – Routers & Switches – Cisco IOS
   ├── MBSS – Exceptions & Waivers Register
   └── MBSS – Automation Backlog
   ```
2. **Rule Register columns** (same on all four platform pages):
   Rule ID · Rule Name · Domain · Description / Requirement · Severity · Expected (Compliant) Value · Current Check (Automation Tool) · Old Check · Automation Status · Last Review (Date / By) · Comments
3. **Rule ID format:** `<PREFIX>-<DOMAIN>-<NNN>`, e.g. `CSCO-MGMT-001`. IDs are never renumbered or reused. To retire a rule, strike through the row and write `RETIRED vX.Y` in Comments.
4. **Domains** (shared across vendors so rules can be compared): MGMT, AAA, CRYPTO, LOG, NTP, SNMP, SVC, BANNER, POL, CTRL, HA, VER.
5. **Status values** (Confluence Status macro colours):
   - Severity: CRITICAL (Red), HIGH (Yellow), MEDIUM (Blue), LOW (Grey)
   - Automation: AUTOMATED (Green), PARTIAL (Yellow), MANUAL (Blue), PLANNED (Purple), NOT FEASIBLE (Grey)
   - Exceptions: ACTIVE, EXPIRING, EXPIRED, CLOSED. Backlog: NOT STARTED, IN PROGRESS, DONE
6. **When the tool's check changes:** move the text from Current Check to Old Check, write the new logic in Current Check, record the reason and date in Comments, and update Last Review.
7. **Platform pages** start with a Page Properties table (versions in scope, rule counts, coverage, owner, review dates). The parent page's **Page Properties Report** reads those tables through the label `mbss-platform`.
8. **Each platform page contains:** a "how to maintain" panel, scope notes, the Rule Register (one EXAMPLE row plus two blank rows), an optional per-rule details expand (pass/fail logic, remediation, review history), a known-limitations table and a change log.
9. **Parent page contains:** document control, scope, status legends, coverage dashboard, cross-vendor control matrix, Rule ID convention, review process, change log and references.

## Files (`confluence-template/`)

| File | What it is |
|---|---|
| `pages.py` | **Source of truth.** All page content as a small block model. Edit here. |
| `build.py` | Renders `pages.py` into the three outputs below. Run `python3 build.py`; it needs only the Python 3 standard library. |
| `kit_template.html` | Template for the preview kit. `build.py` injects the page data into it. |
| `mbss-confluence-kit.html` | Generated preview of all seven pages, with copy buttons. Open it in a browser. |
| `output/wiki/*.txt` | Confluence wiki markup, one file per page |
| `output/storage/*.xml` | Confluence storage format, one file per page |
| `README.md` | Short file overview |

Don't hand-edit anything under `output/` or `mbss-confluence-kit.html`. It is overwritten on every build.

## Which output to paste where

| Confluence | Use | Result |
|---|---|---|
| Cloud | "Copy for Confluence Cloud" button in the kit (rich HTML) | Headings, tables, lists and code come across. Status values arrive as plain text. Grey `[Insert … macro]` lines mark where to add `/toc`, `/page properties` and the report macro. |
| Data Center / Server | `output/wiki/*.txt` via Insert (+) › Markup › Confluence wiki | Status, panel, expand and Page Properties macros come through. |
| Either, via source editor or REST API | `output/storage/*.xml` as `body.storage` | Exact, with every macro. |

## State at handoff

- Lives in the public repo https://github.com/jahithoque/network-mbss (branch `main`). It was originally written in a private research repo; only this project was carried over, without that repo's history.
- Kit published privately as a claude.ai artifact: https://claude.ai/artifact/NPnYKXvxmwBeJdotfbjj8B
- **Verified:** all storage-format files parse as well-formed XML. The kit page has no horizontal scroll at 1400px or 400px, in light or dark mode.
- **Not verified:** nothing has been pasted into a real Confluence yet. The riskiest part is `{status:…|title=…}` macros inside wiki markup table cells, so test one page first.
- **Placeholders:** example rows, CLI snippets and remediation commands are illustrative. Check them against the OS versions in scope. Suggested fix times per severity are marked "e.g." and should follow internal policy.

## Possible next steps (offered, not started)

1. **CSV/Excel → Rule Register converter:** fill a sheet with the 11 columns and generate the full register table in all three formats, with status colours. Useful for 100+ rules.
2. **REST API publisher:** create the seven pages under a parent page, with labels, from `output/storage/` (Cloud v2 API or Data Center v1).
3. **Starter rule sets:** a full set of MBSS rules for one or more platforms, aligned to CIS Benchmarks.

## Getting started

```bash
git clone https://github.com/jahithoque/network-mbss.git
cd network-mbss
python3 confluence-template/build.py
```

Then start Claude Code in the `network-mbss` folder with:

> Read `HANDOFF.md` and `confluence-template/pages.py`. We're continuing the Network MBSS Confluence templates. After any change to `pages.py`, run `python3 confluence-template/build.py`.
