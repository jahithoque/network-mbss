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
