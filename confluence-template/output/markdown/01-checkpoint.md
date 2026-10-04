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
