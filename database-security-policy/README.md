# Database Security Configuration Policy – Confluence pages

Company policy **SEC-POL-DB-001**: the minimum security configuration for company databases, with Tenable compliance scans as the assessment method and CIS Benchmarks as the technical basis.

| Page | Purpose |
|---|---|
| Database Security Configuration Policy (parent) | Policy statement, scope, roles, common baseline, Tenable assessment requirements, remediation timelines, compliance dashboard, cross-platform matrix, exceptions, non-compliance |
| DB Security – Oracle | Control register (`ORA-*`), Tenable setup, control details |
| DB Security – Microsoft SQL Server | 〃 (`MSSQL-*`) |
| DB Security – MySQL | 〃 (`MYSQL-*`) |
| DB Security – MongoDB | 〃 (`MONGO-*`) |
| DB Security – IBM Db2 | 〃 (`DB2-*`) |
| DB Security – Teradata | 〃 (`TD-*`). No CIS Benchmark or native Tenable DB checks: MANUAL until a custom audit is built |
| DB Security – Exceptions Register | Approved, time-limited deviations |

Control register columns: Control ID · Control Name · Domain · Requirement · Severity · Compliant Value ·
Tenable Check (Audit / Query) · CIS Reference · Assessment · Last Review (Date / By) · Comments.

## Files

- `output/database-security-policy-confluence.md`: **start here.** All pages in one Markdown file, with page titles, labels and paste steps at the top
- `dbsec-confluence-kit.html`: open in a browser, pick a page, press **Copy page**, then in Confluence press Ctrl+Shift+D (Insert › Markup) and paste. Cloud copy and storage format too
- `output/wiki/*.txt`: Confluence wiki markup
- `output/storage/*.xml`: Confluence storage format (source editor or REST API `body.storage`)
- `pages.py`: page content (edit here)
- `build.py`: renders `pages.py` into all formats. Run `python3 build.py` after editing (Python 3 standard library only)

## Before approval

- **CIS Reference** cells are placeholders. Fill them from the `reference` field of the Tenable audit file version you scan with; section numbers change between benchmark releases.
- Compliant values follow CIS recommendations, adjusted to company values (14-character passwords, lockout ≤ 5, 90-day expiry, TLS 1.2+). Align them with your corporate password and vulnerability management standards.
- Remediation timelines (15 / 30 / 90 days) are proposals.
- Queries and remediation snippets are examples. Test them on your versions and apply through change management.
- CIS Benchmark text is licensed by CIS. Controls here are written in the company's own words and reference CIS rather than copying it.

## Moving to its own repository

This folder is self-contained. To make it a separate repository:

```bash
git subtree split --prefix=database-security-policy -b dbsec-only
git push git@github.com:<owner>/database-security-policy.git dbsec-only:main
```
