# Network MBSS – Confluence pages

All seven Confluence pages in one file. Each page starts with a heading that is its page title.

## How to paste a page into Confluence Data Center (Windows)

1. Open this file on GitHub, where it shows formatted with real tables.
2. In Confluence, create the page and type its title from the table below. Create **Network MBSS** first and the others as its children.
3. Back on GitHub, select from the line under the page's title down to the end of that page (just above the next page's title), and press `Ctrl+C`.
4. Click in the Confluence page body and press `Ctrl+V`.
5. Add the labels from the table below.

You can also paste the raw Markdown through Insert › Markup › Markdown (`Ctrl+Shift+D`), but Confluence Data Center doesn't always turn Markdown tables into real tables, so check the preview first.

Markdown has no Confluence macros. Status values (HIGH, AUTOMATED, …) are plain text (type `/status` in a cell for a coloured lozenge), the maintenance notes are a quote block, Rule details is a normal section, and the coverage dashboard on the overview is a table you update by hand.

## Pages

| # | Page title | Parent page | Labels |
|---|---|---|---|
| 1 | [Network MBSS](#network-mbss) | (top level) | `mbss` |
| 2 | [MBSS – Firewall – Check Point](#mbss--firewall--check-point) | Network MBSS | `mbss, mbss-platform` |
| 3 | [MBSS – Proxy – BlueCoat ProxySG](#mbss--proxy--bluecoat-proxysg) | Network MBSS | `mbss, mbss-platform` |
| 4 | [MBSS – Load Balancer – F5 BIG-IP](#mbss--load-balancer--f5-big-ip) | Network MBSS | `mbss, mbss-platform` |
| 5 | [MBSS – Routers & Switches – Cisco IOS](#mbss--routers--switches--cisco-ios) | Network MBSS | `mbss, mbss-platform` |
| 6 | [MBSS – Exceptions & Waivers Register](#mbss--exceptions--waivers-register) | Network MBSS | `mbss, mbss-exceptions` |
| 7 | [MBSS – Automation Backlog](#mbss--automation-backlog) | Network MBSS | `mbss, mbss-automation` |

---

# Network MBSS

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

---

# MBSS – Firewall – Check Point

| Property | Value |
|---|---|
| **Platform** | Firewall – Check Point |
| **Vendor / product** | Check Point Security Gateways & Security Management (Gaia OS) |
| **OS versions in scope** | *\[e.g., R81.20, R82\]* |
| **Components in scope** | Gaia OS (gateways), Gaia OS (management server), security policy / rulebase, log server |
| **Rule ID prefix** | `CP` |
| **Devices in scope** | *\[count or link to inventory\]* |
| **Total rules** | 0 |
| **Automated rules** | 0 |
| **Automation coverage** | 0% |
| **Owner team** | *\[Team\]* |
| **Last full review** | YYYY-MM-DD |
| **Next review due** | YYYY-MM-DD |

> **How to maintain this page**
>
> - One row per rule in the Rule Register. Rule IDs are never renumbered or reused.
> - **Current Check**: the command or API the tool runs and the pass condition.
> - **When the tool's check changes**: move the text from Current Check to Old Check, write the new logic in Current Check, give the reason and date in Comments, and update Last Review.
> - To retire a rule, strike through the row and write `RETIRED vX.Y` in Comments.
> - Update the counts in the table above after editing. The coverage dashboard on the overview page uses them.

## Scope & applicability

- Components: Gaia OS (gateways), Gaia OS (management server), security policy / rulebase, log server
- Data source: `clish`: `show configuration`, `show password-controls all`
- Data source: Management API: `mgmt_cli show access-rulebase` (JSON)
- Data source: Expert mode files where no clish/API equivalent exists
- **CP-POL rules** apply to the security policy on the management server, not to individual gateways.
- State in **Comments** when a rule applies only to gateways or only to management servers.
- Note inline layers and shared layers when the rulebase check does not parse them.

## Rule register

| Rule ID | Rule Name | Domain | Description / Requirement | Severity | Expected (Compliant) Value | Current Check (Automation Tool) | Old Check | Automation Status | Last Review (Date / By) | Comments |
|---|---|---|---|---|---|---|---|---|---|---|
| **CP-AAA-001** — *EXAMPLE – delete* | Gaia password minimum length | AAA | Local Gaia accounts must use a minimum password length of 14 characters. | HIGH | `min-password-length` is 14 or higher | clish `show password-controls all`; parse minimum password length; PASS if ≥ 14 | Manual check in Gaia WebUI › User Management › Password Policy | AUTOMATED | 2026-09-30 / Reviewer name | Applies to gateways and management servers. Moved from manual to automated check in v1.1. |
| *\[CP-DOMAIN-NNN\]* | *\[Short rule name\]* | *\[Domain code\]* | *\[What must be true\]* | *\[CRITICAL / HIGH / MEDIUM / LOW\]* | *\[Exact config / value that passes\]* | *\[Command or API + pass condition\]* | *\[Previous check logic, or N/A\]* | *\[AUTOMATED / PARTIAL / MANUAL / PLANNED / NOT FEASIBLE\]* | *\[YYYY-MM-DD / Name\]* | *\[Caveats, reason for check change, exception IDs\]* |
| *\[CP-DOMAIN-NNN\]* | *\[Short rule name\]* | *\[Domain code\]* | *\[What must be true\]* | *\[CRITICAL / HIGH / MEDIUM / LOW\]* | *\[Exact config / value that passes\]* | *\[Command or API + pass condition\]* | *\[Previous check logic, or N/A\]* | *\[AUTOMATED / PARTIAL / MANUAL / PLANNED / NOT FEASIBLE\]* | *\[YYYY-MM-DD / Name\]* | *\[Caveats, reason for check change, exception IDs\]* |

## Rule details

Optional. Copy this expand once per rule that needs more detail than the register holds.

### CP-DOMAIN-NNN – Rule name – details

| Field | Value |
|---|---|
| **Applies to** | *\[All / gateways only / routers only / ...\]* |
| **Rationale / risk** | *\[Why the rule exists; what happens if it is not met\]* |
| **Automation check ID** | *\[ID of the check in the automation tool\]* |
| **Data source / command** | *\[Command, API call or file the tool reads\]* |
| **Parsing method** | *\[Regex / TextFSM / Genie / JSON path\]* |
| **Pass condition** | *\[Exact condition\]* |
| **Fail condition** | *\[Exact condition\]* |
| **Not applicable when** | *\[e.g., feature not licensed or not configured\]* |
| **Remediation impact** | *\[None / session drop / service restart / reboot\]* |
| **Auto-remediation allowed** | *\[Yes / No / With change approval\]* |
| **Reference** | *\[CIS section, internal policy clause, NIST / ISO control\]* |
| **Exceptions** | *\[EXC-IDs, or None\]* |
| **Why the check changed** | *\[Old → current, with date and reason\]* |

**Remediation (example syntax, verify before use):**

```
set password-controls min-password-length 14
save config
```

**Review history**

| Date | Reviewed by | Outcome | Notes |
|---|---|---|---|
| YYYY-MM-DD | *\[Name\]* | *\[No change / check updated / rule updated\]* | *\[Notes\]* |

## Known automation limitations & false positives

| Rule ID | Limitation / false-positive scenario | Impact | Workaround | Jira |
|---|---|---|---|---|
| *\[CP-DOMAIN-NNN\]* | *\[What the tool gets wrong\]* | *\[Missed FAIL / false FAIL\]* | *\[Manual step\]* | *\[KEY-123\]* |

## Page change log

| Version | Date | Author | Change | Approved by |
|---|---|---|---|---|
| 0.1 | YYYY-MM-DD | *\[Name\]* | Initial draft from template | *\[Name\]* |
| *\[x.y\]* | YYYY-MM-DD | *\[Name\]* | *\[What changed\]* | *\[Name\]* |

---

# MBSS – Proxy – BlueCoat ProxySG

| Property | Value |
|---|---|
| **Platform** | Proxy – BlueCoat |
| **Vendor / product** | Symantec BlueCoat ProxySG / Edge SWG (SGOS) |
| **OS versions in scope** | *\[e.g., SGOS 7.3.x\]* |
| **Components in scope** | SGOS system settings, management services, proxy policy (VPM / CPL), authentication realms |
| **Rule ID prefix** | `BC` |
| **Devices in scope** | *\[count or link to inventory\]* |
| **Total rules** | 0 |
| **Automated rules** | 0 |
| **Automation coverage** | 0% |
| **Owner team** | *\[Team\]* |
| **Last full review** | YYYY-MM-DD |
| **Next review due** | YYYY-MM-DD |

> **How to maintain this page**
>
> - One row per rule in the Rule Register. Rule IDs are never renumbered or reused.
> - **Current Check**: the command or API the tool runs and the pass condition.
> - **When the tool's check changes**: move the text from Current Check to Old Check, write the new logic in Current Check, give the reason and date in Comments, and update Last Review.
> - To retire a rule, strike through the row and write `RETIRED vX.Y` in Comments.
> - Update the counts in the table above after editing. The coverage dashboard on the overview page uses them.

## Scope & applicability

- Components: SGOS system settings, management services, proxy policy (VPM / CPL), authentication realms
- Data source: SGOS CLI: `show config`
- Data source: Policy export (VPM / CPL) for policy rules
- Data source: Management Console where no CLI equivalent exists
- **BC-POL rules** are checked against the installed policy, not the VPM draft.
- State in **Comments** when a rule applies only to explicit or only to transparent deployments.

## Rule register

| Rule ID | Rule Name | Domain | Description / Requirement | Severity | Expected (Compliant) Value | Current Check (Automation Tool) | Old Check | Automation Status | Last Review (Date / By) | Comments |
|---|---|---|---|---|---|---|---|---|---|---|
| **BC-MGMT-001** — *EXAMPLE – delete* | Disable Telnet and HTTP management consoles | MGMT | Only encrypted management services (HTTPS-Console, SSH-Console) may be enabled. | HIGH | Telnet-Console and HTTP-Console disabled; HTTPS-Console and SSH-Console enabled | `show config` › management-services section; FAIL if Telnet-Console or HTTP-Console is enabled | Regex matched Telnet-Console only; HTTP-Console was not checked | AUTOMATED | 2026-09-30 / Reviewer name | Old check missed HTTP-Console. Updated in v1.1. |
| *\[BC-DOMAIN-NNN\]* | *\[Short rule name\]* | *\[Domain code\]* | *\[What must be true\]* | *\[CRITICAL / HIGH / MEDIUM / LOW\]* | *\[Exact config / value that passes\]* | *\[Command or API + pass condition\]* | *\[Previous check logic, or N/A\]* | *\[AUTOMATED / PARTIAL / MANUAL / PLANNED / NOT FEASIBLE\]* | *\[YYYY-MM-DD / Name\]* | *\[Caveats, reason for check change, exception IDs\]* |
| *\[BC-DOMAIN-NNN\]* | *\[Short rule name\]* | *\[Domain code\]* | *\[What must be true\]* | *\[CRITICAL / HIGH / MEDIUM / LOW\]* | *\[Exact config / value that passes\]* | *\[Command or API + pass condition\]* | *\[Previous check logic, or N/A\]* | *\[AUTOMATED / PARTIAL / MANUAL / PLANNED / NOT FEASIBLE\]* | *\[YYYY-MM-DD / Name\]* | *\[Caveats, reason for check change, exception IDs\]* |

## Rule details

Optional. Copy this expand once per rule that needs more detail than the register holds.

### BC-DOMAIN-NNN – Rule name – details

| Field | Value |
|---|---|
| **Applies to** | *\[All / gateways only / routers only / ...\]* |
| **Rationale / risk** | *\[Why the rule exists; what happens if it is not met\]* |
| **Automation check ID** | *\[ID of the check in the automation tool\]* |
| **Data source / command** | *\[Command, API call or file the tool reads\]* |
| **Parsing method** | *\[Regex / TextFSM / Genie / JSON path\]* |
| **Pass condition** | *\[Exact condition\]* |
| **Fail condition** | *\[Exact condition\]* |
| **Not applicable when** | *\[e.g., feature not licensed or not configured\]* |
| **Remediation impact** | *\[None / session drop / service restart / reboot\]* |
| **Auto-remediation allowed** | *\[Yes / No / With change approval\]* |
| **Reference** | *\[CIS section, internal policy clause, NIST / ISO control\]* |
| **Exceptions** | *\[EXC-IDs, or None\]* |
| **Why the check changed** | *\[Old → current, with date and reason\]* |

**Remediation (example syntax, verify before use):**

```
#(config) management-services
#(config management-services) disable Telnet-Console
#(config management-services) disable HTTP-Console
```

**Review history**

| Date | Reviewed by | Outcome | Notes |
|---|---|---|---|
| YYYY-MM-DD | *\[Name\]* | *\[No change / check updated / rule updated\]* | *\[Notes\]* |

## Known automation limitations & false positives

| Rule ID | Limitation / false-positive scenario | Impact | Workaround | Jira |
|---|---|---|---|---|
| *\[BC-DOMAIN-NNN\]* | *\[What the tool gets wrong\]* | *\[Missed FAIL / false FAIL\]* | *\[Manual step\]* | *\[KEY-123\]* |

## Page change log

| Version | Date | Author | Change | Approved by |
|---|---|---|---|---|
| 0.1 | YYYY-MM-DD | *\[Name\]* | Initial draft from template | *\[Name\]* |
| *\[x.y\]* | YYYY-MM-DD | *\[Name\]* | *\[What changed\]* | *\[Name\]* |

---

# MBSS – Load Balancer – F5 BIG-IP

| Property | Value |
|---|---|
| **Platform** | Load Balancer – F5 BIG-IP |
| **Vendor / product** | F5 BIG-IP (LTM / GTM / ASM / APM) on TMOS |
| **OS versions in scope** | *\[e.g., 15.1.x, 17.1.x\]* |
| **Components in scope** | TMOS system & management, management port and self IPs, LTM objects (virtual servers, profiles, SSL), provisioned modules |
| **Rule ID prefix** | `F5` |
| **Devices in scope** | *\[count or link to inventory\]* |
| **Total rules** | 0 |
| **Automated rules** | 0 |
| **Automation coverage** | 0% |
| **Owner team** | *\[Team\]* |
| **Last full review** | YYYY-MM-DD |
| **Next review due** | YYYY-MM-DD |

> **How to maintain this page**
>
> - One row per rule in the Rule Register. Rule IDs are never renumbered or reused.
> - **Current Check**: the command or API the tool runs and the pass condition.
> - **When the tool's check changes**: move the text from Current Check to Old Check, write the new logic in Current Check, give the reason and date in Comments, and update Last Review.
> - To retire a rule, strike through the row and write `RETIRED vX.Y` in Comments.
> - Update the counts in the table above after editing. The coverage dashboard on the overview page uses them.

## Scope & applicability

- Components: TMOS system & management, management port and self IPs, LTM objects (virtual servers, profiles, SSL), provisioned modules
- Data source: `tmsh list sys ...`, `tmsh list ltm ...`
- Data source: iControl REST, e.g. `/mgmt/tm/sys/sshd`
- Data source: `bigip.conf` / `bigip_base.conf` from UCS backups
- State in **Comments** when a rule applies only to a module (ASM, APM) or only to specific partitions.
- Note vCMP guest vs host applicability where it differs.

## Rule register

| Rule ID | Rule Name | Domain | Description / Requirement | Severity | Expected (Compliant) Value | Current Check (Automation Tool) | Old Check | Automation Status | Last Review (Date / By) | Comments |
|---|---|---|---|---|---|---|---|---|---|---|
| **F5-MGMT-001** — *EXAMPLE – delete* | Restrict SSH management access | MGMT | SSH to the BIG-IP must be limited to approved management subnets. | HIGH | `sys sshd allow` lists only approved management subnets; never `ALL` | `tmsh list sys sshd allow`; FAIL if `ALL` or any subnet not in the approved list | `tmsh list sys sshd allow`; FAIL only if value is `ALL` | AUTOMATED | 2026-09-30 / Reviewer name | Approved subnet list is kept in the automation tool's variables file. |
| *\[F5-DOMAIN-NNN\]* | *\[Short rule name\]* | *\[Domain code\]* | *\[What must be true\]* | *\[CRITICAL / HIGH / MEDIUM / LOW\]* | *\[Exact config / value that passes\]* | *\[Command or API + pass condition\]* | *\[Previous check logic, or N/A\]* | *\[AUTOMATED / PARTIAL / MANUAL / PLANNED / NOT FEASIBLE\]* | *\[YYYY-MM-DD / Name\]* | *\[Caveats, reason for check change, exception IDs\]* |
| *\[F5-DOMAIN-NNN\]* | *\[Short rule name\]* | *\[Domain code\]* | *\[What must be true\]* | *\[CRITICAL / HIGH / MEDIUM / LOW\]* | *\[Exact config / value that passes\]* | *\[Command or API + pass condition\]* | *\[Previous check logic, or N/A\]* | *\[AUTOMATED / PARTIAL / MANUAL / PLANNED / NOT FEASIBLE\]* | *\[YYYY-MM-DD / Name\]* | *\[Caveats, reason for check change, exception IDs\]* |

## Rule details

Optional. Copy this expand once per rule that needs more detail than the register holds.

### F5-DOMAIN-NNN – Rule name – details

| Field | Value |
|---|---|
| **Applies to** | *\[All / gateways only / routers only / ...\]* |
| **Rationale / risk** | *\[Why the rule exists; what happens if it is not met\]* |
| **Automation check ID** | *\[ID of the check in the automation tool\]* |
| **Data source / command** | *\[Command, API call or file the tool reads\]* |
| **Parsing method** | *\[Regex / TextFSM / Genie / JSON path\]* |
| **Pass condition** | *\[Exact condition\]* |
| **Fail condition** | *\[Exact condition\]* |
| **Not applicable when** | *\[e.g., feature not licensed or not configured\]* |
| **Remediation impact** | *\[None / session drop / service restart / reboot\]* |
| **Auto-remediation allowed** | *\[Yes / No / With change approval\]* |
| **Reference** | *\[CIS section, internal policy clause, NIST / ISO control\]* |
| **Exceptions** | *\[EXC-IDs, or None\]* |
| **Why the check changed** | *\[Old → current, with date and reason\]* |

**Remediation (example syntax, verify before use):**

```
tmsh modify sys sshd allow replace-all-with { 10.10.0.0/24 }
tmsh save sys config
```

**Review history**

| Date | Reviewed by | Outcome | Notes |
|---|---|---|---|
| YYYY-MM-DD | *\[Name\]* | *\[No change / check updated / rule updated\]* | *\[Notes\]* |

## Known automation limitations & false positives

| Rule ID | Limitation / false-positive scenario | Impact | Workaround | Jira |
|---|---|---|---|---|
| *\[F5-DOMAIN-NNN\]* | *\[What the tool gets wrong\]* | *\[Missed FAIL / false FAIL\]* | *\[Manual step\]* | *\[KEY-123\]* |

## Page change log

| Version | Date | Author | Change | Approved by |
|---|---|---|---|---|
| 0.1 | YYYY-MM-DD | *\[Name\]* | Initial draft from template | *\[Name\]* |
| *\[x.y\]* | YYYY-MM-DD | *\[Name\]* | *\[What changed\]* | *\[Name\]* |

---

# MBSS – Routers & Switches – Cisco IOS

| Property | Value |
|---|---|
| **Platform** | Routers & Switches – Cisco IOS |
| **Vendor / product** | Cisco IOS and IOS-XE routers and switches |
| **OS versions in scope** | *\[e.g., IOS 15.2(x), IOS-XE 17.x\]* |
| **Components in scope** | Routers, L3 switches, L2 access switches |
| **Rule ID prefix** | `CSCO` |
| **Devices in scope** | *\[count or link to inventory\]* |
| **Total rules** | 0 |
| **Automated rules** | 0 |
| **Automation coverage** | 0% |
| **Owner team** | *\[Team\]* |
| **Last full review** | YYYY-MM-DD |
| **Next review due** | YYYY-MM-DD |

> **How to maintain this page**
>
> - One row per rule in the Rule Register. Rule IDs are never renumbered or reused.
> - **Current Check**: the command or API the tool runs and the pass condition.
> - **When the tool's check changes**: move the text from Current Check to Old Check, write the new logic in Current Check, give the reason and date in Comments, and update Last Review.
> - To retire a rule, strike through the row and write `RETIRED vX.Y` in Comments.
> - Update the counts in the table above after editing. The coverage dashboard on the overview page uses them.

## Scope & applicability

- Components: Routers, L3 switches, L2 access switches
- Data source: `show running-config`, `show version`, `show ip ssh`
- Data source: Parsed with regex, TextFSM or Genie (state which one in the rule detail)
- State in **Comments** when a rule applies only to routers, only to L3 switches or only to access switches.
- Note rules that differ between IOS and IOS-XE syntax.

## Rule register

| Rule ID | Rule Name | Domain | Description / Requirement | Severity | Expected (Compliant) Value | Current Check (Automation Tool) | Old Check | Automation Status | Last Review (Date / By) | Comments |
|---|---|---|---|---|---|---|---|---|---|---|
| **CSCO-MGMT-001** — *EXAMPLE – delete* | Allow only SSHv2 on VTY lines | MGMT | Remote management must use SSH version 2. Telnet must be disabled on all VTY lines. | HIGH | `ip ssh version 2` and `transport input ssh` under every `line vty` | Parse `show running-config`: PASS if `ip ssh version 2` is present AND every `line vty` block has `transport input ssh` only | Regex for `ip ssh version 2` only; VTY transport not checked | AUTOMATED | 2026-09-30 / Reviewer name | Old check passed devices that still allowed Telnet on vty 5 15. |
| *\[CSCO-DOMAIN-NNN\]* | *\[Short rule name\]* | *\[Domain code\]* | *\[What must be true\]* | *\[CRITICAL / HIGH / MEDIUM / LOW\]* | *\[Exact config / value that passes\]* | *\[Command or API + pass condition\]* | *\[Previous check logic, or N/A\]* | *\[AUTOMATED / PARTIAL / MANUAL / PLANNED / NOT FEASIBLE\]* | *\[YYYY-MM-DD / Name\]* | *\[Caveats, reason for check change, exception IDs\]* |
| *\[CSCO-DOMAIN-NNN\]* | *\[Short rule name\]* | *\[Domain code\]* | *\[What must be true\]* | *\[CRITICAL / HIGH / MEDIUM / LOW\]* | *\[Exact config / value that passes\]* | *\[Command or API + pass condition\]* | *\[Previous check logic, or N/A\]* | *\[AUTOMATED / PARTIAL / MANUAL / PLANNED / NOT FEASIBLE\]* | *\[YYYY-MM-DD / Name\]* | *\[Caveats, reason for check change, exception IDs\]* |

## Rule details

Optional. Copy this expand once per rule that needs more detail than the register holds.

### CSCO-DOMAIN-NNN – Rule name – details

| Field | Value |
|---|---|
| **Applies to** | *\[All / gateways only / routers only / ...\]* |
| **Rationale / risk** | *\[Why the rule exists; what happens if it is not met\]* |
| **Automation check ID** | *\[ID of the check in the automation tool\]* |
| **Data source / command** | *\[Command, API call or file the tool reads\]* |
| **Parsing method** | *\[Regex / TextFSM / Genie / JSON path\]* |
| **Pass condition** | *\[Exact condition\]* |
| **Fail condition** | *\[Exact condition\]* |
| **Not applicable when** | *\[e.g., feature not licensed or not configured\]* |
| **Remediation impact** | *\[None / session drop / service restart / reboot\]* |
| **Auto-remediation allowed** | *\[Yes / No / With change approval\]* |
| **Reference** | *\[CIS section, internal policy clause, NIST / ISO control\]* |
| **Exceptions** | *\[EXC-IDs, or None\]* |
| **Why the check changed** | *\[Old → current, with date and reason\]* |

**Remediation (example syntax, verify before use):**

```
ip ssh version 2
line vty 0 15
 transport input ssh
```

**Review history**

| Date | Reviewed by | Outcome | Notes |
|---|---|---|---|
| YYYY-MM-DD | *\[Name\]* | *\[No change / check updated / rule updated\]* | *\[Notes\]* |

## Known automation limitations & false positives

| Rule ID | Limitation / false-positive scenario | Impact | Workaround | Jira |
|---|---|---|---|---|
| *\[CSCO-DOMAIN-NNN\]* | *\[What the tool gets wrong\]* | *\[Missed FAIL / false FAIL\]* | *\[Manual step\]* | *\[KEY-123\]* |

## Page change log

| Version | Date | Author | Change | Approved by |
|---|---|---|---|---|
| 0.1 | YYYY-MM-DD | *\[Name\]* | Initial draft from template | *\[Name\]* |
| *\[x.y\]* | YYYY-MM-DD | *\[Name\]* | *\[What changed\]* | *\[Name\]* |

---

# MBSS – Exceptions & Waivers Register

> **Before you add an exception**
>
> - Every exception needs an expiry date and a named risk owner.
> - Exclude the device from the automation tool's check for that rule, and record that in **Excluded in tool?**.
> - Put the Exception ID in the Comments column of the rule on its platform page.

## Status

| Status | Meaning |
|---|---|
| ACTIVE | Approved and within its expiry date |
| EXPIRING | Expires within 30 days; renew or remediate |
| EXPIRED | Past expiry; the device is non-compliant |
| CLOSED | Remediated or no longer needed |

## Register

| Exception ID | Rule ID | Platform | Affected devices | Business justification | Compensating control | Risk accepted by | Approved on | Expires on | Excluded in tool? | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| **EXC-001** | *\[CSCO-MGMT-001\]* | *\[Cisco IOS\]* | *\[Hostnames / group\]* | *\[Why it can't comply\]* | *\[What reduces the risk\]* | *\[Name, role\]* | YYYY-MM-DD | YYYY-MM-DD | *\[Yes / No\]* | ACTIVE |

---

# MBSS – Automation Backlog

Every rule whose Automation Status is PARTIAL, MANUAL or PLANNED has a row here.

> **Jira**
>
> If the work is tracked in Jira, add a Jira Issues macro below this panel filtered on the label `mbss-automation`.

## Backlog

| Rule ID | Platform | Current status | Gap (why not fully automated) | Proposed check | Owner | Target date | Jira | Progress |
|---|---|---|---|---|---|---|---|---|
| *\[CP-POL-002\]* | *\[Check Point\]* | PARTIAL | *\[e.g., inline layers not parsed\]* | *\[Command / API + logic\]* | *\[Name\]* | YYYY-MM-DD | *\[KEY-123\]* | NOT STARTED |

## Progress status

| Status | Meaning |
|---|---|
| NOT STARTED | Not picked up |
| IN PROGRESS | Check being built or tested |
| DONE | Live in the tool; platform page updated |
