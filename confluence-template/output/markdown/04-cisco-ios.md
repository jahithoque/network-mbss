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
