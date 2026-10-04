# Network MBSS

Confluence page templates for Minimum Baseline Security Standards (MBSS) on network devices: Check Point firewalls, Symantec BlueCoat ProxySG, F5 BIG-IP and Cisco IOS / IOS-XE.

- [`confluence-template/`](confluence-template/): page content, the build script and the generated outputs (see its README)
- [`HANDOFF.md`](HANDOFF.md): design decisions, current state and next steps

```bash
python3 confluence-template/build.py   # regenerate outputs after editing pages.py
```

Example rules and commands are illustrative placeholders. Verify them against your own OS versions and policy.
