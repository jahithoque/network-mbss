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
