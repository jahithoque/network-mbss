# Network MBSS

Confluence page templates for Minimum Baseline Security Standards (MBSS) on network devices: Check Point firewalls, Symantec BlueCoat ProxySG, F5 BIG-IP and Cisco IOS / IOS-XE.

- **[`network-mbss-confluence.md`](confluence-template/output/network-mbss-confluence.md): start here.** All seven Confluence pages in one Markdown file, with page titles, labels and Windows paste steps at the top
- [`confluence-template/`](confluence-template/): page content, the build script and the other generated outputs (see its README)
- [`HANDOFF.md`](HANDOFF.md): design decisions, current state and next steps

```bash
python3 confluence-template/build.py   # regenerate outputs after editing pages.py
```

Example rules and commands are illustrative placeholders. Verify them against your own OS versions and policy.

## Database Security Configuration Policy

[`database-security-policy/`](database-security-policy/) holds company policy SEC-POL-DB-001 for Oracle, SQL Server, MySQL, MongoDB, IBM Db2 and Teradata: CIS-based controls assessed with Tenable. **Start with [`database-security-policy-confluence.md`](database-security-policy/output/database-security-policy-confluence.md).** The folder is self-contained so it can be split into its own repository (see its README).
