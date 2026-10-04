| Property | Value |
|---|---|
| **Document owner** | *\[Name / team\]* |
| **Approver** | *\[Name\]* |
| **Version** | 0.1 |
| **Document status** | DRAFT |
| **Effective date** | YYYY-MM-DD |
| **Next review due** | YYYY-MM-DD |
| **Classification** | *\[Internal / Confidential\]* |

## Purpose

This space defines the Minimum Baseline Security Standard (MBSS) for network devices. Each rule states the required configuration, how the Network Automation tool checks it today, and how the check has changed over time.

## Scope

| Category | Vendor / product | OS versions in scope | Devices | Page | Owner team |
|---|---|---|---|---|---|
| Firewall | Check Point Security Gateways & Security Management (Gaia OS) | *\[e.g., R81.20, R82\]* | *\[count\]* | MBSS – Firewall – Check Point | *\[Team\]* |
| Proxy | Symantec BlueCoat ProxySG / Edge SWG (SGOS) | *\[e.g., SGOS 7.3.x\]* | *\[count\]* | MBSS – Proxy – BlueCoat ProxySG | *\[Team\]* |
| Load Balancer | F5 BIG-IP (LTM / GTM / ASM / APM) on TMOS | *\[e.g., 15.1.x, 17.1.x\]* | *\[count\]* | MBSS – Load Balancer – F5 BIG-IP | *\[Team\]* |
| Routers & Switches | Cisco IOS and IOS-XE routers and switches | *\[e.g., IOS 15.2(x), IOS-XE 17.x\]* | *\[count\]* | MBSS – Routers & Switches – Cisco IOS | *\[Team\]* |

**Out of scope:** *\[List excluded device types, lab devices, etc.\]*

## How to read this standard

### Severity

| Severity | Meaning | Target fix time (align with policy) |
|---|---|---|
| CRITICAL | Direct path to compromise or outage | e.g., 7 days |
| HIGH | Significant weakness in access, crypto or logging | e.g., 30 days |
| MEDIUM | Hardening gap with limited direct exposure | e.g., 90 days |
| LOW | Best practice or hygiene item | e.g., next change window |

### Automation status

| Status | Meaning |
|---|---|
| AUTOMATED | The automation tool checks the full requirement |
| PARTIAL | The tool checks part of the requirement. The gap is described in Comments |
| MANUAL | An engineer checks it during the review |
| PLANNED | Automation is in the backlog (see MBSS – Automation Backlog) |
| NOT FEASIBLE | Can't be verified from configuration or API output |

## Coverage dashboard

Copy these numbers from the summary table at the top of each platform page whenever its rules change.

| Platform | Total | Automated | Partial | Manual | Planned | Not feasible | Coverage % | Last full review |
|---|---|---|---|---|---|---|---|---|
| Check Point | 0 | 0 | 0 | 0 | 0 | 0 | 0% | YYYY-MM-DD |
| BlueCoat | 0 | 0 | 0 | 0 | 0 | 0 | 0% | YYYY-MM-DD |
| F5 BIG-IP | 0 | 0 | 0 | 0 | 0 | 0 | 0% | YYYY-MM-DD |
| Cisco IOS | 0 | 0 | 0 | 0 | 0 | 0 | 0% | YYYY-MM-DD |

## Cross-vendor control matrix

Enter the Rule ID for each platform, or N/A. Leave a cell empty only while the rule is still being written.

| Control | Check Point | BlueCoat | F5 BIG-IP | Cisco IOS |
|---|---|---|---|---|
| Encrypted management only (SSH / HTTPS) | – | – | – | – |
| Management access restricted (ACL / allow-list) | – | – | – | – |
| Centralized AAA (TACACS+ / RADIUS) | – | – | – | – |
| Local account password policy | – | – | – | – |
| Remote syslog configured | – | – | – | – |
| NTP from approved servers | – | – | – | – |
| SNMPv3 only, no default communities | – | – | – | – |
| Login warning banner | – | – | – | – |
| Unused services disabled | – | – | – | – |
| Approved software version | – | – | – | – |
| Configuration backup | – | – | – | – |

## Rule ID convention

Format: `<PREFIX>-<DOMAIN>-<NNN>`, for example `CSCO-MGMT-001`. Prefixes: `CP` Check Point, `BC` BlueCoat, `F5` F5 BIG-IP, `CSCO` Cisco IOS. Rule IDs are never renumbered or reused.

| Domain code | Domain | Typical controls |
|---|---|---|
| `MGMT` | Management plane access | SSH/HTTPS only, management ACLs or allow-lists, session timeouts |
| `AAA` | Authentication & authorization | TACACS+/RADIUS, local fallback account, password policy, RBAC |
| `CRYPTO` | Cryptography | TLS versions, cipher suites, key lengths, certificate validity |
| `LOG` | Logging & monitoring | Remote syslog, log levels, timestamps, audit logging |
| `NTP` | Time synchronization | Approved NTP servers, NTP authentication |
| `SNMP` | SNMP | SNMPv3 only, no default communities, ACL-restricted |
| `SVC` | Service hardening | Unused services disabled (HTTP server, CDP, Telnet, small servers) |
| `BANNER` | Legal banners | Login / MOTD warning banner |
| `POL` | Policy / rulebase | No any-any rules, cleanup rule, logging on rules, default deny |
| `CTRL` | Control plane | Control-plane policing, routing protocol authentication |
| `HA` | Availability & backup | HA sync, configuration backup |
| `VER` | Software & patching | Approved OS version, end-of-life / end-of-support |

## Review process

- **Scheduled review:** *\[quarterly\]*. Update Last Review on every rule you review, even if nothing changed.
- **Also review after:** a major OS upgrade, a new CIS Benchmark release, a change to the automation tool's check logic, or an audit finding.
- **When a check changes:** copy Current Check into Old Check, write the new logic in Current Check, and give the reason and date in Comments.
- **Exceptions** go in MBSS – Exceptions & Waivers Register, not in the rule tables.

## Change log

| Version | Date | Author | Change | Approved by |
|---|---|---|---|---|
| 0.1 | YYYY-MM-DD | *\[Name\]* | Initial draft from template | *\[Name\]* |
| *\[x.y\]* | YYYY-MM-DD | *\[Name\]* | *\[What changed\]* | *\[Name\]* |

## References

- CIS Benchmarks (Cisco IOS, Check Point Firewall, F5 BIG-IP): https://www.cisecurity.org/cis-benchmarks
- Vendor hardening guides: *\[add links\]*
- Internal network security policy: *\[add link\]*
- Network Automation tool documentation / repository: *\[add link\]*
