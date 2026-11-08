# Database Security Configuration Policy – Confluence pages

Company policy SEC-POL-DB-001 and its platform standards (Oracle, Microsoft SQL Server, MySQL, MongoDB, IBM Db2, Teradata), with Tenable as the assessment method and CIS Benchmarks as the technical basis. Each page starts with a heading that is its page title.

## How to paste a page into Confluence (Windows)

1. Open this file on GitHub, where it shows formatted with real tables.
2. In Confluence, create the page and type its title from the table below. Create **Database Security Configuration Policy** first and the others as its children.
3. Back on GitHub, select from the line under the page's title down to the end of that page (just above the next page's title), and press `Ctrl+C`.
4. Click in the Confluence page body and press `Ctrl+V`.
5. Add the labels from the table below.

Markdown has no Confluence macros: status values (HIGH, AUTOMATED, …) are plain text, the policy banner is a quote, and the compliance dashboard is a table you update by hand. For real macros use the wiki markup in `output/wiki/` (Insert › Markup, `Ctrl+Shift+D`) or the preview kit `dbsec-confluence-kit.html`.

## Pages

| # | Page title | Parent page | Labels |
|---|---|---|---|
| 1 | [Database Security Configuration Policy](#database-security-configuration-policy) | (top level) | `dbsec, company-policy` |
| 2 | [DB Security – Oracle](#db-security--oracle) | Database Security Configuration Policy | `dbsec, dbsec-platform, company-policy` |
| 3 | [DB Security – Microsoft SQL Server](#db-security--microsoft-sql-server) | Database Security Configuration Policy | `dbsec, dbsec-platform, company-policy` |
| 4 | [DB Security – MySQL](#db-security--mysql) | Database Security Configuration Policy | `dbsec, dbsec-platform, company-policy` |
| 5 | [DB Security – MongoDB](#db-security--mongodb) | Database Security Configuration Policy | `dbsec, dbsec-platform, company-policy` |
| 6 | [DB Security – IBM Db2](#db-security--ibm-db2) | Database Security Configuration Policy | `dbsec, dbsec-platform, company-policy` |
| 7 | [DB Security – Teradata](#db-security--teradata) | Database Security Configuration Policy | `dbsec, dbsec-platform, company-policy` |
| 8 | [DB Security – Exceptions Register](#db-security--exceptions-register) | Database Security Configuration Policy | `dbsec, dbsec-exceptions` |

---

# Database Security Configuration Policy

| Property | Value |
|---|---|
| **Policy ID** | `SEC-POL-DB-001` |
| **Policy type** | Company policy – technical security standard |
| **Policy owner** | *\[CISO / Head of Information Security\]* |
| **Maintained by** | *\[Database Engineering & Security Architecture\]* |
| **Approver** | *\[Name, role\]* |
| **Version** | 0.1 |
| **Policy status** | DRAFT |
| **Effective date** | YYYY-MM-DD |
| **Next review due** | YYYY-MM-DD (12 months after approval) |
| **Classification** | Internal |

> **Company policy – SEC-POL-DB-001**
>
> This page is part of the company Database Security Configuration Policy (SEC-POL-DB-001). Its requirements are mandatory for every database in scope. Deviations need an approved entry in the DB Security – Exceptions Register. CIS Benchmarks and Tenable audit files are the technical basis and assessment method; where this policy differs from CIS, this policy applies.

## 1. Purpose

This policy sets the minimum security configuration for every company database. It protects the confidentiality, integrity and availability of company and customer data, and gives auditors one place to see each requirement, how Tenable assesses it, and the current compliance status.

## 2. Policy statement

- Every database in scope **must** be configured to meet the controls on its platform page before it goes into production, and must stay compliant for its whole life.
- Database configuration compliance **must** be assessed with Tenable using the approved audit files on the schedule in section 6.
- Failed controls **must** be remediated within the timelines in section 7, or covered by an approved, time-limited exception.
- New database platforms or major versions **must not** go into production until a platform page for them is approved.

## 3. Scope

All database instances owned or operated by the company, or operated for it by a third party, in production, DR, UAT and development environments, on-premises or in the cloud (IaaS). Managed database services (PaaS) are in scope for the controls the company can configure.

| Platform | Product | Versions in scope | Technical basis | Control prefix | Platform page |
|---|---|---|---|---|---|
| Oracle | Oracle Database (single instance, RAC, Data Guard; CDB and PDBs) | *\[e.g., 19c, 23ai\]* | CIS Oracle Database 19c Benchmark (use the 23ai benchmark for 23ai) | `ORA` | DB Security – Oracle |
| Microsoft SQL Server | Microsoft SQL Server (Database Engine, on Windows or Linux; Always On availability groups) | *\[e.g., 2019, 2022\]* | CIS Microsoft SQL Server 2019 / 2022 Benchmark | `MSSQL` | DB Security – Microsoft SQL Server |
| MySQL | MySQL Community / Enterprise Server (InnoDB Cluster, replication) | *\[e.g., 8.0, 8.4 LTS\]* | CIS Oracle MySQL Community / Enterprise Server 8.0 Benchmark | `MYSQL` | DB Security – MySQL |
| MongoDB | MongoDB Community / Enterprise Server (replica sets, sharded clusters) | *\[e.g., 7.0, 8.0\]* | CIS MongoDB 7 / 8 Benchmark | `MONGO` | DB Security – MongoDB |
| IBM Db2 | IBM Db2 for Linux, UNIX and Windows (LUW), including HADR | *\[e.g., 11.5.x\]* | CIS IBM Db2 11 Benchmark | `DB2` | DB Security – IBM Db2 |
| Teradata | Teradata Vantage (on-premises / VantageCore, VantageCloud Enterprise) | *\[e.g., 17.20, 20.00\]* | No CIS Benchmark is published. Company baseline derived from the Teradata Vantage Security Administration guide and DB-COM controls | `TD` | DB Security – Teradata |

**Out of scope:** *\[e.g., embedded databases inside vendor appliances, developer workstations, decommissioned systems\]*

## 4. Roles and responsibilities

| Role | Responsibilities |
|---|---|
| **Policy owner (CISO)** | Approves the policy and exceptions rated CRITICAL; reports compliance to the risk committee |
| **Database Engineering / DBAs** | Build databases to this policy, remediate findings, keep platform pages and control values current |
| **Vulnerability Management (Tenable)** | Maintain scan policies, audit files and credentials; run scans; publish compliance results |
| **Application / data owners** | Approve access, classify data, accept risk for exceptions on their systems |
| **Security Operations (SOC)** | Receive and monitor database audit logs in the SIEM |
| **Internal Audit** | Independently test compliance with this policy |

## 5. Common baseline (all platforms)

Every platform page implements these company-wide requirements. Platform pages may be stricter, never weaker.

| ID | Domain | Requirement | Minimum value |
|---|---|---|---|
| **DB-COM-01** | `VER` | Run a vendor-supported release and apply security patches within the patch SLA. | No end-of-support versions; latest security patch level minus one at most |
| **DB-COM-02** | `AAA` | Change, lock or remove every vendor default and sample account. | No account with a default or blank password |
| **DB-COM-03** | `AAA` | Human administrators authenticate with named accounts through central directory (AD / LDAP / Kerberos) where the platform supports it. | No shared admin logons; break-glass account vaulted in PAM |
| **DB-COM-04** | `AAA` | Local database accounts follow the corporate password standard. | Min. 14 characters, complexity on, lockout after ≤ 5 failures, expiry ≤ 90 days for human accounts, reuse history ≥ 10 |
| **DB-COM-05** | `PRIV` | Grant privileges through roles on least privilege. Nothing beyond vendor defaults to PUBLIC / guest. | Admin roles limited to the approved DBA group; quarterly access review |
| **DB-COM-06** | `CRYPTO` | Encrypt all client and replication traffic. | TLS 1.2 or higher (or native network encryption with AES-256); plaintext listeners disabled |
| **DB-COM-07** | `CRYPTO` | Encrypt data at rest for databases classified Confidential or higher. | TDE / native encryption, or encrypted volumes with keys outside the DB host |
| **DB-COM-08** | `LOG` | Audit logons (success and failure), privilege and security changes, and DDL. Forward to the SIEM. | Audit enabled; retained ≥ 12 months (90 days online) |
| **DB-COM-09** | `NET` | Expose the database only to the application and admin networks that need it. | Bound to required interfaces; host / network firewall allow-list |
| **DB-COM-10** | `SVC` | Disable features that execute OS commands, read files or open network connections unless approved. | Off by default; approved exceptions only |
| **DB-COM-11** | `OS` | Run database services under a dedicated, non-root / non-administrator account. No credentials in clear text in files or scripts. | Dedicated service account; config files readable only by the service account |
| **DB-COM-12** | `BKP` | Encrypt backups and test restores. | Encrypted backups; restore test at least annually |

## 6. Compliance assessment with Tenable

| Item | Requirement |
|---|---|
| **Scan template** | Tenable **Policy Compliance Auditing** (credentialed), with the audit files listed on each platform page |
| **Audit files** | CIS-based Tenable audit files, tailored to the company values on the platform pages. Tailored copies are version-controlled and the version is recorded on each platform page |
| **Credentials** | Dedicated read-only scan account per platform (privileges on each platform page), stored in Tenable / PAM, never a DBA account |
| **Frequency** | Production: monthly and after every major change or upgrade. Non-production: quarterly. New builds: before go-live |
| **Targets** | Asset lists synchronized from the CMDB database inventory; every instance in scope is scanned |
| **Compliance target** | 100% of CRITICAL and HIGH controls passing (or covered by an exception); ≥ 95% of all controls |
| **Results** | Published to the compliance dashboard below; failed controls raise remediation tickets for the owning team |
| **Manual controls** | Controls marked MANUAL / PARTIAL are reviewed quarterly; evidence is attached to the review ticket |

## 7. Severity, remediation and status legend

### Severity and remediation timelines

| Severity | Meaning | Remediate within (production) | Remediate within (non-production) |
|---|---|---|---|
| CRITICAL | Direct path to unauthorized access or data exposure | 15 days | 30 days |
| HIGH | Significant weakness in authentication, privileges, encryption or auditing | 30 days | 60 days |
| MEDIUM | Hardening gap with limited direct exposure | 90 days | 120 days |
| LOW | Best practice or hygiene item | Next maintenance window | Next maintenance window |

*Timelines run from the Tenable scan date that first reports the failure. Align them with the corporate vulnerability management standard before approval.*

### Assessment status

| Status | Meaning |
|---|---|
| AUTOMATED | The Tenable audit fully assesses the requirement; PASS / FAIL comes from the scan |
| PARTIAL | Tenable collects the data but a reviewer completes the check (e.g., against an approved list) |
| MANUAL | A DBA or reviewer collects evidence by hand during the review |
| PLANNED | A custom audit check is being built |
| NOT FEASIBLE | Cannot be assessed from the database or host; evidence is collected another way |

## 8. Compliance dashboard

Copy these numbers from the summary table at the top of each platform page after every scan.

| Platform | Controls | Automated | Partial | Manual / planned | Compliance % (last scan) | Open CRITICAL / HIGH | Last scan |
|---|---|---|---|---|---|---|---|
| Oracle | 13 | 9 | 4 | 0 | 0% | 0 | YYYY-MM-DD |
| Microsoft SQL Server | 15 | 10 | 5 | 0 | 0% | 0 | YYYY-MM-DD |
| MySQL | 12 | 7 | 5 | 0 | 0% | 0 | YYYY-MM-DD |
| MongoDB | 11 | 7 | 4 | 0 | 0% | 0 | YYYY-MM-DD |
| IBM Db2 | 11 | 7 | 4 | 0 | 0% | 0 | YYYY-MM-DD |
| Teradata | 10 | 0 | 0 | 10 | 0% | 0 | YYYY-MM-DD |

## 9. Cross-platform control matrix

Platform controls that implement each common baseline requirement. A gap means the requirement is assessed by another process (e.g., backups by the backup standard, host hardening by the OS standard) or a control still has to be written.

| Baseline | Requirement | Oracle | Microsoft SQL Server | MySQL | MongoDB | IBM Db2 | Teradata |
|---|---|---|---|---|---|---|---|
| **DB-COM-01** | Run a vendor-supported release and apply security patches within the patch SLA. | ORA-VER-001 | MSSQL-VER-001 | MYSQL-VER-001 | MONGO-VER-001 | DB2-VER-001 | TD-VER-001 |
| **DB-COM-02** | Change, lock or remove every vendor default and sample account. | ORA-AAA-001, ORA-SVC-002 | MSSQL-AAA-002 | MYSQL-AAA-001, MYSQL-SVC-002 | MONGO-AAA-001 | *\[Gap – add control or N/A\]* | TD-AAA-001 |
| **DB-COM-03** | Human administrators authenticate with named accounts through central directory (AD / LDAP / Kerberos) where the platform supports it. | ORA-AAA-003, ORA-AAA-004 | MSSQL-AAA-001 | *\[Gap – add control or N/A\]* | MONGO-AAA-002, MONGO-AAA-003 | DB2-AAA-001, DB2-AAA-002 | TD-AAA-003 |
| **DB-COM-04** | Local database accounts follow the corporate password standard. | ORA-AAA-002 | MSSQL-AAA-003 | MYSQL-AAA-002, MYSQL-AAA-003 | *\[Gap – add control or N/A\]* | *\[Gap – add control or N/A\]* | TD-AAA-002 |
| **DB-COM-05** | Grant privileges through roles on least privilege. Nothing beyond vendor defaults to PUBLIC / guest. | ORA-PRIV-001, ORA-PRIV-002 | MSSQL-PRIV-001, MSSQL-PRIV-002, MSSQL-PRIV-003 | MYSQL-PRIV-001 | MONGO-PRIV-001 | DB2-PRIV-001, DB2-PRIV-002, DB2-PRIV-003 | TD-PRIV-001, TD-PRIV-002 |
| **DB-COM-06** | Encrypt all client and replication traffic. | ORA-CRYPTO-001 | MSSQL-CRYPTO-001 | MYSQL-CRYPTO-001 | MONGO-CRYPTO-001 | DB2-CRYPTO-001 | TD-CRYPTO-001 |
| **DB-COM-07** | Encrypt data at rest for databases classified Confidential or higher. | ORA-CRYPTO-002 | MSSQL-CRYPTO-002 | *\[Gap – add control or N/A\]* | MONGO-CRYPTO-002 | DB2-CRYPTO-002 | TD-CRYPTO-002 |
| **DB-COM-08** | Audit logons (success and failure), privilege and security changes, and DDL. Forward to the SIEM. | ORA-LOG-001 | MSSQL-LOG-001 | MYSQL-LOG-001 | MONGO-LOG-001 | DB2-LOG-001 | TD-LOG-001 |
| **DB-COM-09** | Expose the database only to the application and admin networks that need it. | ORA-NET-001 | MSSQL-NET-001 | *\[Gap – add control or N/A\]* | MONGO-NET-001 | DB2-NET-001 | TD-NET-001 |
| **DB-COM-10** | Disable features that execute OS commands, read files or open network connections unless approved. | ORA-PRIV-001, ORA-SVC-001 | MSSQL-SVC-001, MSSQL-SVC-002, MSSQL-SVC-003 | MYSQL-SVC-001, MYSQL-SVC-003 | MONGO-SVC-001 | *\[Gap – add control or N/A\]* | *\[Gap – add control or N/A\]* |
| **DB-COM-11** | Run database services under a dedicated, non-root / non-administrator account. No credentials in clear text in files or scripts. | *\[Gap – add control or N/A\]* | MSSQL-OS-001 | MYSQL-OS-001, MYSQL-OS-002 | MONGO-OS-001 | DB2-OS-001 | *\[Gap – add control or N/A\]* |
| **DB-COM-12** | Encrypt backups and test restores. | *\[Gap – add control or N/A\]* | *\[Gap – add control or N/A\]* | *\[Gap – add control or N/A\]* | *\[Gap – add control or N/A\]* | *\[Gap – add control or N/A\]* | *\[Gap – add control or N/A\]* |

## 10. Exceptions

- Any control that cannot be met needs an exception in **DB Security – Exceptions Register** before the remediation deadline.
- Exceptions have a named risk owner, a compensating control and an expiry date of at most 12 months.
- CRITICAL exceptions are approved by the policy owner; others by the Head of Database Engineering and the application owner.
- Approved exceptions are applied as exclusions in Tenable so they are not reported as failures, and are re-reviewed at expiry.

## 11. Non-compliance

Overdue findings without an approved exception are escalated to the system owner's management and reported to the risk committee. Databases with open CRITICAL findings may be isolated from the network. Wilful breach of this policy may lead to disciplinary action under the company code of conduct.

## 12. Control ID convention

Format: `<PREFIX>-<DOMAIN>-<NNN>`, for example `ORA-AAA-001`. Prefixes: ORA Oracle, MSSQL Microsoft SQL Server, MYSQL MySQL, MONGO MongoDB, DB2 IBM Db2, TD Teradata. Control IDs are never renumbered or reused; retired controls are struck through with `RETIRED vX.Y` in Comments.

| Domain code | Domain | Typical controls |
|---|---|---|
| `VER` | Software & patching | Vendor-supported release, security patches / release updates applied |
| `AAA` | Authentication | Default accounts, password policy, lockout, central authentication |
| `PRIV` | Authorization & privileges | Least privilege, PUBLIC / guest rights, admin role membership |
| `CRYPTO` | Encryption | TLS in transit, encryption at rest, key management |
| `LOG` | Auditing & logging | Database audit trail, failed / successful logons, forwarding to SIEM |
| `NET` | Network exposure | Listener / bind address, ports, remote administration |
| `SVC` | Features & configuration | Dangerous features disabled, sample databases removed, secure parameters |
| `OS` | Host & file system | Service account, file permissions, no clear-text credentials on disk |
| `BKP` | Backup & recovery | Encrypted backups, restore testing |

## 13. Policy review

- This policy is reviewed at least **annually** and approved by the policy owner.
- Platform pages are also reviewed after a new CIS Benchmark or Tenable audit file release, a major database version, or an audit finding.
- When a new benchmark version is adopted, record the benchmark and audit file versions on the platform page and update the CIS Reference column.

## 14. Change log

| Version | Date | Author | Change | Approved by |
|---|---|---|---|---|
| 0.1 | YYYY-MM-DD | *\[Name\]* | Initial draft | *\[Name\]* |
| *\[x.y\]* | YYYY-MM-DD | *\[Name\]* | *\[What changed\]* | *\[Name\]* |

## 15. References

- CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks (basis for control values; licence terms apply to benchmark content)
- Tenable compliance audit files: https://www.tenable.com/audits
- Corporate Information Security Policy: *\[add link\]*
- Corporate password standard: *\[add link\]*
- Vulnerability management standard (remediation SLAs): *\[add link\]*
- Data classification standard: *\[add link\]*

---

# DB Security – Oracle

| Property | Value |
|---|---|
| **Platform** | Oracle |
| **Product** | Oracle Database (single instance, RAC, Data Guard; CDB and PDBs) |
| **Versions in scope** | *\[e.g., 19c, 23ai\]* |
| **Policy** | `SEC-POL-DB-001` |
| **Technical basis** | CIS Oracle Database 19c Benchmark (use the 23ai benchmark for 23ai) |
| **Tenable audit file(s)** | CIS\_Oracle\_Database\_19c\_\*.audit (database checks) + CIS Unix audit for listener / file checks |
| **Tenable credential** | Database credential, type Oracle (SID or service name; scan each PDB as well as the CDB) |
| **Control prefix** | `ORA` |
| **Instances in scope** | *\[count or link to CMDB\]* |
| **Controls** | 13 |
| **Automated (Tenable)** | 9 of 13 |
| **Compliance % (last scan)** | 0% |
| **Open CRITICAL / HIGH** | 0 |
| **Last Tenable scan** | YYYY-MM-DD |
| **Owner team** | *\[Team\]* |
| **Next review due** | YYYY-MM-DD |

> **Company policy – SEC-POL-DB-001**
>
> This page is part of the company Database Security Configuration Policy (SEC-POL-DB-001). Its requirements are mandatory for every database in scope. Deviations need an approved entry in the DB Security – Exceptions Register. CIS Benchmarks and Tenable audit files are the technical basis and assessment method; where this policy differs from CIS, this policy applies.

## Scope & applicability

- Apply database-level controls to the CDB root and to every PDB. State in Comments if a control is CDB-only.
- Listener and `sqlnet.ora` controls are checked through the Unix (SSH) part of the scan on the database host.
- Oracle Autonomous / managed cloud services: controls the provider manages are N/A; record them in Comments.

## Tenable assessment setup

| Item | Value |
|---|---|
| **Scan template** | Policy Compliance Auditing (credentialed) |
| **Audit file(s)** | CIS\_Oracle\_Database\_19c\_\*.audit (database checks) + CIS Unix audit for listener / file checks |
| **Credential** | Database credential, type Oracle (SID or service name; scan each PDB as well as the CDB) |
| **Scan account privileges** | `CREATE SESSION`, `SELECT ANY DICTIONARY` (or `SELECT_CATALOG_ROLE`), `AUDIT_VIEWER`; no DBA role |
| **Tailoring** | Company values from the register below override CIS defaults in the tailored audit file. Store it in *\[repository / Tenable policy name\]* |

## Control register

> **How to maintain this register**
>
> - One row per control. Control IDs are never renumbered or reused.
> - **Tenable Check** describes what the audit item reads and its pass condition. Copy the CIS section from the audit item's `reference` field into **CIS Reference**.
> - Changing a Compliant Value is a policy change: record it in the change log and get approval.
> - After every scan, update Compliance % and Open CRITICAL / HIGH in the table at the top of the page.

| Control ID | Control Name | Domain | Requirement | Severity | Compliant Value | Tenable Check (Audit / Query) | CIS Reference | Assessment | Last Review (Date / By) | Comments |
|---|---|---|---|---|---|---|---|---|---|---|
| **ORA-VER-001** | Supported release with current Release Update | `VER` | The database runs a release under Oracle Premier or Extended Support with a Release Update no older than the previous quarterly CPU. | CRITICAL | Latest or previous quarterly RU in `DBA_REGISTRY_SQLPATCH` | `SELECT banner_full FROM v$version` and latest `DBA_REGISTRY_SQLPATCH` entry; compared with the approved RU list | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* | Tenable reports the version; the approved RU list is maintained by the DBA team. |
| **ORA-AAA-001** | No default passwords | `AAA` | No account may use an Oracle default password. Unused Oracle-supplied accounts are locked and expired. | CRITICAL | `SELECT * FROM dba_users_with_defpwd` returns no rows | Query `DBA_USERS_WITH_DEFPWD`; FAIL on any row | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **ORA-AAA-002** | Password and lockout profile | `AAA` | Every profile used by a non-service account enforces the corporate password standard and a verify function. | HIGH | `FAILED_LOGIN_ATTEMPTS` ≤ 5, `PASSWORD_LOCK_TIME` ≥ 1, `PASSWORD_LIFE_TIME` ≤ 90, `PASSWORD_REUSE_MAX` ≥ 10, `PASSWORD_GRACE_TIME` ≤ 5, `PASSWORD_VERIFY_FUNCTION` not NULL | Query `DBA_PROFILES` for each profile assigned in `DBA_USERS` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* | Service accounts use a separate profile with no expiry; their passwords are rotated by PAM. |
| **ORA-AAA-003** | Remote OS authentication disabled | `AAA` | The database must not trust the client operating system to authenticate users or roles. | HIGH | `REMOTE_OS_AUTHENT` / `REMOTE_OS_ROLES` = FALSE, `OS_ROLES` = FALSE | Query `v$parameter` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **ORA-AAA-004** | Password file restricted | `AAA` | Remote SYSDBA logon through a password file is allowed only where a documented need exists (e.g., Data Guard). | MEDIUM | `REMOTE_LOGIN_PASSWORDFILE` = NONE, or EXCLUSIVE with an approved exception | Query `v$parameter` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **ORA-PRIV-001** | No PUBLIC execute on network and file packages | `PRIV` | PUBLIC must not have EXECUTE on packages that read files, open network connections or run dynamic SQL / Java. | HIGH | No PUBLIC grant on `UTL_FILE`, `UTL_TCP`, `UTL_HTTP`, `UTL_SMTP`, `UTL_INADDR`, `DBMS_JAVA`, `DBMS_SCHEDULER`, `DBMS_LOB` | Query `DBA_TAB_PRIVS WHERE grantee='PUBLIC'` for the package list | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **ORA-PRIV-002** | Powerful privileges restricted | `PRIV` | \*ANY\* system privileges, DBA, and administrative privileges (SYSDBA, SYSOPER, SYSBACKUP…) are granted only to approved accounts. | HIGH | Grantees in `DBA_SYS_PRIVS` / `DBA_ROLE_PRIVS` / `v$pwfile_users` match the approved list | Tenable lists grantees; reviewer compares with the approved list | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* | Tenable cannot know the approved list; record the review outcome here. |
| **ORA-SVC-001** | Security initialization parameters | `SVC` | Security-related initialization parameters are set to the company values. | MEDIUM | `SEC_MAX_FAILED_LOGIN_ATTEMPTS` ≤ 3, `SEC_PROTOCOL_ERROR_FURTHER_ACTION` = (DROP,3), `SEC_RETURN_SERVER_RELEASE_BANNER` = FALSE, `SQL92_SECURITY` = TRUE, `_TRACE_FILES_PUBLIC` = FALSE, `RESOURCE_LIMIT` = TRUE | Query `v$parameter` / `x$ksppcv` for hidden parameters | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **ORA-SVC-002** | Sample schemas removed | `SVC` | Sample schemas (HR, OE, SH, PM, IX, BI, SCOTT) are not installed in production databases. | LOW | No sample schema in `DBA_USERS` | Query `DBA_USERS` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **ORA-NET-001** | Listener hardened | `NET` | The listener cannot be reconfigured at run time and does not offer external procedures. | HIGH | `ADMIN_RESTRICTIONS_<listener>=ON` in `listener.ora`; no `EXTPROC` entry | Unix audit: content check on `$ORACLE_HOME/network/admin/listener.ora` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **ORA-CRYPTO-001** | Network encryption required | `CRYPTO` | All client connections are encrypted with TLS or Oracle native network encryption. | HIGH | `SQLNET.ENCRYPTION_SERVER = REQUIRED`, `SQLNET.ENCRYPTION_TYPES_SERVER = (AES256)`, or TCPS only with TLS 1.2+ | Unix audit: content check on `sqlnet.ora` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **ORA-CRYPTO-002** | Encryption at rest (TDE) | `CRYPTO` | Databases classified Confidential or higher use TDE tablespace encryption with the keystore outside the data files. | HIGH | Keystore OPEN in `v$encryption_wallet`; user tablespaces ENCRYPTED = YES | Query `v$encryption_wallet` and `DBA_TABLESPACES` | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* | Tenable cannot see data classification; scope comes from the CMDB. |
| **ORA-LOG-001** | Unified auditing policies | `LOG` | Unified auditing records logons, privilege use and security-relevant changes and is forwarded to the SIEM. | HIGH | Policies enabled in `AUDIT_UNIFIED_ENABLED_POLICIES` cover LOGON / LOGOFF, `ORA_SECURECONFIG`, `ORA_ACCOUNT_MGMT`, `ORA_DATABASE_PARAMETER` | Query `AUDIT_UNIFIED_ENABLED_POLICIES` | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* | SIEM forwarding is confirmed manually by the SOC. |
| *\[ORA-DOMAIN-NNN\]* | *\[Short control name\]* | *\[Domain\]* | *\[What must be true\]* | *\[CRITICAL / HIGH / MEDIUM / LOW\]* | *\[Value that passes\]* | *\[Audit item / query + pass condition\]* | *\[CIS §\]* | *\[AUTOMATED / PARTIAL / MANUAL / PLANNED / NOT FEASIBLE\]* | *\[YYYY-MM-DD / Name\]* | *\[Caveats, exception IDs\]* |

## Control details

Optional. Copy this expand for each control that needs more detail than the register holds.

### ORA-VER-001 – Supported release with current Release Update – details (example)

| Field | Value |
|---|---|
| **Applies to** | *\[All instances / production only / CDB only / ...\]* |
| **Rationale / risk** | *\[Why the control exists; what happens if it is not met\]* |
| **Tenable audit item** | *\[Description string of the check in the .audit file\]* |
| **Audit file and version** | *\[File name, version, date\]* |
| **Check type** | *\[SQL query / config file / registry / manual\]* |
| **Pass condition** | *\[Exact condition\]* |
| **Not applicable when** | *\[e.g., feature not installed or not licensed\]* |
| **Remediation impact** | *\[None / restart required / application change\]* |
| **CIS reference** | *\[Benchmark name, version, section\]* |
| **Exceptions** | *\[EXC-IDs, or None\]* |

**Evidence query (example, verify before use):**

```
SELECT username, account_status
  FROM dba_users_with_defpwd d JOIN dba_users u USING (username);
```

**Remediation (example, apply through change management):**

```
ALTER USER <username> PASSWORD EXPIRE ACCOUNT LOCK;
-- or set a new password if the account is required
```

**Review history**

| Date | Reviewed by | Outcome | Notes |
|---|---|---|---|
| YYYY-MM-DD | *\[Name\]* | *\[Compliant / remediated / exception raised\]* | *\[Notes\]* |

## Known Tenable limitations & false positives

| Control ID | Limitation / false-positive scenario | Impact | Workaround |
|---|---|---|---|
| *\[ORA-DOMAIN-NNN\]* | *\[What the audit gets wrong\]* | *\[Missed FAIL / false FAIL\]* | *\[Manual step or audit tailoring\]* |

## Page change log

| Version | Date | Author | Change | Approved by |
|---|---|---|---|---|
| 0.1 | YYYY-MM-DD | *\[Name\]* | Initial draft | *\[Name\]* |
| *\[x.y\]* | YYYY-MM-DD | *\[Name\]* | *\[What changed\]* | *\[Name\]* |

---

# DB Security – Microsoft SQL Server

| Property | Value |
|---|---|
| **Platform** | Microsoft SQL Server |
| **Product** | Microsoft SQL Server (Database Engine, on Windows or Linux; Always On availability groups) |
| **Versions in scope** | *\[e.g., 2019, 2022\]* |
| **Policy** | `SEC-POL-DB-001` |
| **Technical basis** | CIS Microsoft SQL Server 2019 / 2022 Benchmark |
| **Tenable audit file(s)** | CIS\_Microsoft\_SQL\_Server\_2022\_\*.audit (database checks) + Windows audit for registry / service checks |
| **Tenable credential** | Database credential, type SQL Server (Windows or SQL authentication; one entry per instance / port) |
| **Control prefix** | `MSSQL` |
| **Instances in scope** | *\[count or link to CMDB\]* |
| **Controls** | 15 |
| **Automated (Tenable)** | 10 of 15 |
| **Compliance % (last scan)** | 0% |
| **Open CRITICAL / HIGH** | 0 |
| **Last Tenable scan** | YYYY-MM-DD |
| **Owner team** | *\[Team\]* |
| **Next review due** | YYYY-MM-DD |

> **Company policy – SEC-POL-DB-001**
>
> This page is part of the company Database Security Configuration Policy (SEC-POL-DB-001). Its requirements are mandatory for every database in scope. Deviations need an approved entry in the DB Security – Exceptions Register. CIS Benchmarks and Tenable audit files are the technical basis and assessment method; where this policy differs from CIS, this policy applies.

## Scope & applicability

- Instance-level controls apply to every instance, including named instances and SSRS / SSAS hosts where a Database Engine is installed.
- Database-level controls (guest, TRUSTWORTHY, TDE) apply to every user database; system databases are noted in Comments.
- Azure SQL Database / Managed Instance: controls the platform enforces are N/A.

## Tenable assessment setup

| Item | Value |
|---|---|
| **Scan template** | Policy Compliance Auditing (credentialed) |
| **Audit file(s)** | CIS\_Microsoft\_SQL\_Server\_2022\_\*.audit (database checks) + Windows audit for registry / service checks |
| **Credential** | Database credential, type SQL Server (Windows or SQL authentication; one entry per instance / port) |
| **Scan account privileges** | `VIEW SERVER STATE`, `VIEW ANY DEFINITION`, `CONNECT ANY DATABASE` (2014+), membership of the user role in `msdb`; no sysadmin |
| **Tailoring** | Company values from the register below override CIS defaults in the tailored audit file. Store it in *\[repository / Tenable policy name\]* |

## Control register

> **How to maintain this register**
>
> - One row per control. Control IDs are never renumbered or reused.
> - **Tenable Check** describes what the audit item reads and its pass condition. Copy the CIS section from the audit item's `reference` field into **CIS Reference**.
> - Changing a Compliant Value is a policy change: record it in the change log and get approval.
> - After every scan, update Compliance % and Open CRITICAL / HIGH in the table at the top of the page.

| Control ID | Control Name | Domain | Requirement | Severity | Compliant Value | Tenable Check (Audit / Query) | CIS Reference | Assessment | Last Review (Date / By) | Comments |
|---|---|---|---|---|---|---|---|---|---|---|
| **MSSQL-VER-001** | Supported version with latest CU / GDR | `VER` | The instance runs a supported version with the latest security update (CU or GDR) within the patch SLA. | CRITICAL | `SERVERPROPERTY('ProductUpdateLevel')` matches the approved build list | `SELECT @@VERSION`; compared with the approved build list | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* | Tenable vulnerability plugins also flag missing updates. |
| **MSSQL-AAA-001** | Windows authentication mode | `AAA` | Instances use Windows Authentication only. Mixed mode needs an approved exception. | HIGH | `SERVERPROPERTY('IsIntegratedSecurityOnly')` = 1 | Query `SERVERPROPERTY` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MSSQL-AAA-002** | sa disabled and renamed | `AAA` | The built-in sa login (principal\_id 1) is disabled and renamed. | HIGH | `sys.server_principals` where `principal_id = 1`: `is_disabled = 1`, name ≠ 'sa' | Query `sys.server_principals` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MSSQL-AAA-003** | SQL logins follow password policy | `AAA` | Every SQL-authenticated login enforces the Windows password policy; expiration is enforced for logins in sysadmin. | HIGH | `is_policy_checked = 1` for all SQL logins; `is_expiration_checked = 1` for sysadmin members | Query `sys.sql_logins` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MSSQL-SVC-001** | xp\_cmdshell disabled | `SVC` | xp\_cmdshell must be disabled. | CRITICAL | `xp_cmdshell` value\_in\_use = 0 | Query `sys.configurations` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MSSQL-SVC-002** | Surface-area options disabled | `SVC` | Server options that extend the attack surface are disabled unless approved. | HIGH | value\_in\_use = 0 for `Ad Hoc Distributed Queries`, `clr enabled`, `cross db ownership chaining`, `Database Mail XPs`, `Ole Automation Procedures`, `remote access`, `scan for startup procs`; `clr strict security` = 1 | Query `sys.configurations` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* | Database Mail is often required; record approved instances as exceptions. |
| **MSSQL-SVC-003** | Remote DAC restricted | `SVC` | The remote dedicated admin connection is off, except on clustered instances where it is needed. | MEDIUM | `remote admin connections` = 0 (1 allowed on failover cluster instances) | Query `sys.configurations` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MSSQL-PRIV-001** | guest has no CONNECT in user databases | `PRIV` | The guest user cannot connect to any database other than master, tempdb and msdb. | HIGH | No `CONNECT` granted to guest in user databases | Query `sys.database_permissions` in each database | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MSSQL-PRIV-002** | PUBLIC role has only default permissions | `PRIV` | No permissions are granted to the public server role beyond the defaults; sysadmin members match the approved list. | HIGH | Only default public grants (VIEW ANY DATABASE, CONNECT on default endpoints) | Query `sys.server_permissions` for grantee\_principal\_id = 2; list sysadmin members | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* | sysadmin membership is compared with the approved list by the reviewer. |
| **MSSQL-PRIV-003** | TRUSTWORTHY off | `PRIV` | TRUSTWORTHY is OFF for every user database. | HIGH | `is_trustworthy_on = 0` (msdb excepted) | Query `sys.databases` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MSSQL-NET-001** | Instance not advertised | `NET` | The instance is hidden from SQL Browser enumeration and does not listen on the default port where feasible. | LOW | HideInstance = 1; static port other than 1433 | Windows audit: registry check under `MSSQLServer\SuperSocketNetLib` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MSSQL-CRYPTO-001** | Forced TLS encryption | `CRYPTO` | Client connections are encrypted with TLS 1.2 or higher using a trusted certificate. | HIGH | ForceEncryption = 1; TLS 1.0 / 1.1 disabled in SCHANNEL | Windows audit: registry check on `SuperSocketNetLib\ForceEncryption` and SCHANNEL protocols | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MSSQL-CRYPTO-002** | TDE for confidential databases | `CRYPTO` | Databases classified Confidential or higher use Transparent Data Encryption; certificates are backed up off-host. | HIGH | `sys.dm_database_encryption_keys` encryption\_state = 3 | Query `sys.dm_database_encryption_keys` | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* | Data classification comes from the CMDB. |
| **MSSQL-LOG-001** | Login and security auditing | `LOG` | Failed and successful logins and security changes are audited and forwarded to the SIEM. | HIGH | Server audit spec with `FAILED_LOGIN_GROUP`, `SUCCESSFUL_LOGIN_GROUP`, `AUDIT_CHANGE_GROUP`; login auditing = Both | Query `sys.server_audit_specification_details`; registry AuditLevel = 3 | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* | SIEM forwarding is confirmed manually by the SOC. |
| **MSSQL-OS-001** | Dedicated low-privilege service accounts | `OS` | Each SQL Server service runs under its own virtual, managed or domain account that is not a local or domain administrator. | MEDIUM | Service accounts not in local Administrators; one account per service | `sys.dm_server_services` + Windows audit group membership check | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* |   |
| *\[MSSQL-DOMAIN-NNN\]* | *\[Short control name\]* | *\[Domain\]* | *\[What must be true\]* | *\[CRITICAL / HIGH / MEDIUM / LOW\]* | *\[Value that passes\]* | *\[Audit item / query + pass condition\]* | *\[CIS §\]* | *\[AUTOMATED / PARTIAL / MANUAL / PLANNED / NOT FEASIBLE\]* | *\[YYYY-MM-DD / Name\]* | *\[Caveats, exception IDs\]* |

## Control details

Optional. Copy this expand for each control that needs more detail than the register holds.

### MSSQL-VER-001 – Supported version with latest CU / GDR – details (example)

| Field | Value |
|---|---|
| **Applies to** | *\[All instances / production only / CDB only / ...\]* |
| **Rationale / risk** | *\[Why the control exists; what happens if it is not met\]* |
| **Tenable audit item** | *\[Description string of the check in the .audit file\]* |
| **Audit file and version** | *\[File name, version, date\]* |
| **Check type** | *\[SQL query / config file / registry / manual\]* |
| **Pass condition** | *\[Exact condition\]* |
| **Not applicable when** | *\[e.g., feature not installed or not licensed\]* |
| **Remediation impact** | *\[None / restart required / application change\]* |
| **CIS reference** | *\[Benchmark name, version, section\]* |
| **Exceptions** | *\[EXC-IDs, or None\]* |

**Evidence query (example, verify before use):**

```
SELECT name, CAST(value_in_use AS int) AS value_in_use
  FROM sys.configurations
 WHERE name IN ('xp_cmdshell', 'clr enabled', 'Ole Automation Procedures');
```

**Remediation (example, apply through change management):**

```
EXEC sp_configure 'show advanced options', 1; RECONFIGURE;
EXEC sp_configure 'xp_cmdshell', 0; RECONFIGURE;
EXEC sp_configure 'show advanced options', 0; RECONFIGURE;
```

**Review history**

| Date | Reviewed by | Outcome | Notes |
|---|---|---|---|
| YYYY-MM-DD | *\[Name\]* | *\[Compliant / remediated / exception raised\]* | *\[Notes\]* |

## Known Tenable limitations & false positives

| Control ID | Limitation / false-positive scenario | Impact | Workaround |
|---|---|---|---|
| *\[MSSQL-DOMAIN-NNN\]* | *\[What the audit gets wrong\]* | *\[Missed FAIL / false FAIL\]* | *\[Manual step or audit tailoring\]* |

## Page change log

| Version | Date | Author | Change | Approved by |
|---|---|---|---|---|
| 0.1 | YYYY-MM-DD | *\[Name\]* | Initial draft | *\[Name\]* |
| *\[x.y\]* | YYYY-MM-DD | *\[Name\]* | *\[What changed\]* | *\[Name\]* |

---

# DB Security – MySQL

| Property | Value |
|---|---|
| **Platform** | MySQL |
| **Product** | MySQL Community / Enterprise Server (InnoDB Cluster, replication) |
| **Versions in scope** | *\[e.g., 8.0, 8.4 LTS\]* |
| **Policy** | `SEC-POL-DB-001` |
| **Technical basis** | CIS Oracle MySQL Community / Enterprise Server 8.0 Benchmark |
| **Tenable audit file(s)** | CIS\_MySQL\_8.0\_\*.audit (database checks) + Unix audit for my.cnf and file permission checks |
| **Tenable credential** | Database credential, type MySQL (TCP port; one entry per instance) |
| **Control prefix** | `MYSQL` |
| **Instances in scope** | *\[count or link to CMDB\]* |
| **Controls** | 12 |
| **Automated (Tenable)** | 7 of 12 |
| **Compliance % (last scan)** | 0% |
| **Open CRITICAL / HIGH** | 0 |
| **Last Tenable scan** | YYYY-MM-DD |
| **Owner team** | *\[Team\]* |
| **Next review due** | YYYY-MM-DD |

> **Company policy – SEC-POL-DB-001**
>
> This page is part of the company Database Security Configuration Policy (SEC-POL-DB-001). Its requirements are mandatory for every database in scope. Deviations need an approved entry in the DB Security – Exceptions Register. CIS Benchmarks and Tenable audit files are the technical basis and assessment method; where this policy differs from CIS, this policy applies.

## Scope & applicability

- MariaDB and Percona Server are in scope with this page as the baseline; differences are noted in Comments.
- Configuration-file controls (`my.cnf`) are checked through the Unix (SSH) part of the scan.
- Managed services (Amazon RDS / Aurora, Azure Database for MySQL): host and file controls are N/A.

## Tenable assessment setup

| Item | Value |
|---|---|
| **Scan template** | Policy Compliance Auditing (credentialed) |
| **Audit file(s)** | CIS\_MySQL\_8.0\_\*.audit (database checks) + Unix audit for my.cnf and file permission checks |
| **Credential** | Database credential, type MySQL (TCP port; one entry per instance) |
| **Scan account privileges** | `SELECT` on `mysql.*` and `performance_schema.*`, `PROCESS`; no SUPER or administrative grants |
| **Tailoring** | Company values from the register below override CIS defaults in the tailored audit file. Store it in *\[repository / Tenable policy name\]* |

## Control register

> **How to maintain this register**
>
> - One row per control. Control IDs are never renumbered or reused.
> - **Tenable Check** describes what the audit item reads and its pass condition. Copy the CIS section from the audit item's `reference` field into **CIS Reference**.
> - Changing a Compliant Value is a policy change: record it in the change log and get approval.
> - After every scan, update Compliance % and Open CRITICAL / HIGH in the table at the top of the page.

| Control ID | Control Name | Domain | Requirement | Severity | Compliant Value | Tenable Check (Audit / Query) | CIS Reference | Assessment | Last Review (Date / By) | Comments |
|---|---|---|---|---|---|---|---|---|---|---|
| **MYSQL-VER-001** | Supported release with security patches | `VER` | The server runs a supported release (8.0 until its EOL, or 8.4 LTS) at the latest patch level within the patch SLA. | CRITICAL | `SELECT VERSION()` in the approved version list | `SELECT VERSION()` | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* |   |
| **MYSQL-AAA-001** | No anonymous or wildcard admin accounts | `AAA` | No anonymous accounts exist; root and admin accounts cannot log in from any host. | CRITICAL | No row with `user = ''`; root only on `localhost`; no admin with `host = '%'` | Query `mysql.user` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MYSQL-AAA-002** | Password validation component | `AAA` | Password strength validation enforces the corporate password standard. | HIGH | `validate_password.length` ≥ 14, `validate_password.policy` = MEDIUM or STRONG, `password_history` ≥ 10, `default_password_lifetime` ≤ 90 | `SHOW GLOBAL VARIABLES LIKE 'validate_password%'` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* | Service accounts may use PASSWORD EXPIRE NEVER when the password is rotated by PAM. |
| **MYSQL-AAA-003** | Failed-login lockout | `AAA` | Accounts lock after repeated failed logins (8.0.19+), or connection-control throttling is enabled. | MEDIUM | `FAILED_LOGIN_ATTEMPTS` ≤ 5 and `PASSWORD_LOCK_TIME` ≥ 1 on human accounts | Query `mysql.user.User_attributes` | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* |   |
| **MYSQL-PRIV-001** | Administrative privileges restricted | `PRIV` | FILE, SUPER, PROCESS, SHUTDOWN, CREATE USER, GRANT OPTION and dynamic admin privileges are held only by approved admin accounts. | HIGH | Grantees match the approved admin list | Query `mysql.user` and `mysql.global_grants` | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* | Tenable lists grantees; the reviewer compares with the approved list. |
| **MYSQL-SVC-001** | Local file loading disabled | `SVC` | Clients cannot load local files into the server, and server-side file import / export is limited to one directory. | HIGH | `local_infile = 0`; `secure_file_priv` set to a dedicated directory or NULL | `SHOW GLOBAL VARIABLES` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MYSQL-SVC-002** | Test database and sample data removed | `SVC` | The test database and any sample schemas are removed. | LOW | `SHOW DATABASES` has no `test` database | `SHOW DATABASES` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MYSQL-SVC-003** | Strict SQL mode | `SVC` | The server rejects invalid data instead of silently truncating it. | LOW | `sql_mode` includes `STRICT_ALL_TABLES` or `STRICT_TRANS_TABLES` | `SELECT @@GLOBAL.sql_mode` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MYSQL-CRYPTO-001** | Secure transport required | `CRYPTO` | All client and replication connections use TLS 1.2 or higher. | HIGH | `require_secure_transport = ON`; `tls_version = TLSv1.2,TLSv1.3` | `SHOW GLOBAL VARIABLES LIKE '%tls%'` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MYSQL-LOG-001** | Error and audit logging | `LOG` | The error log is written to a protected location and an audit log plugin / component records connections and privilege changes. | HIGH | `log_error` set; audit log plugin active (Enterprise Audit, Percona or MariaDB audit plugin) | `SHOW PLUGINS` / `SHOW GLOBAL VARIABLES LIKE 'log_error%'` | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* | Community Edition has no bundled audit plugin; record the approved alternative. |
| **MYSQL-OS-001** | Dedicated service account and file permissions | `OS` | mysqld runs as a dedicated non-root account; data directory and config files are readable only by that account. | MEDIUM | `mysqld` runs as `mysql`; `datadir` mode 750 or stricter; `my.cnf` not world-writable | Unix audit: process owner and file permission checks | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MYSQL-OS-002** | No clear-text passwords on disk or in environment | `OS` | Passwords are not stored in my.cnf, scripts, shell history or the MYSQL\_PWD variable. Use the login path or a vault. | HIGH | No `password=` in option files; `MYSQL_PWD` unset | Unix audit: content check on option files | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* |   |
| *\[MYSQL-DOMAIN-NNN\]* | *\[Short control name\]* | *\[Domain\]* | *\[What must be true\]* | *\[CRITICAL / HIGH / MEDIUM / LOW\]* | *\[Value that passes\]* | *\[Audit item / query + pass condition\]* | *\[CIS §\]* | *\[AUTOMATED / PARTIAL / MANUAL / PLANNED / NOT FEASIBLE\]* | *\[YYYY-MM-DD / Name\]* | *\[Caveats, exception IDs\]* |

## Control details

Optional. Copy this expand for each control that needs more detail than the register holds.

### MYSQL-VER-001 – Supported release with security patches – details (example)

| Field | Value |
|---|---|
| **Applies to** | *\[All instances / production only / CDB only / ...\]* |
| **Rationale / risk** | *\[Why the control exists; what happens if it is not met\]* |
| **Tenable audit item** | *\[Description string of the check in the .audit file\]* |
| **Audit file and version** | *\[File name, version, date\]* |
| **Check type** | *\[SQL query / config file / registry / manual\]* |
| **Pass condition** | *\[Exact condition\]* |
| **Not applicable when** | *\[e.g., feature not installed or not licensed\]* |
| **Remediation impact** | *\[None / restart required / application change\]* |
| **CIS reference** | *\[Benchmark name, version, section\]* |
| **Exceptions** | *\[EXC-IDs, or None\]* |

**Evidence query (example, verify before use):**

```
SELECT user, host FROM mysql.user
 WHERE user = '' OR (host = '%' AND user IN ('root', 'admin'));
```

**Remediation (example, apply through change management):**

```
DROP USER ''@'localhost';
DROP USER ''@'%';
RENAME USER 'root'@'%' TO 'root'@'localhost';
```

**Review history**

| Date | Reviewed by | Outcome | Notes |
|---|---|---|---|
| YYYY-MM-DD | *\[Name\]* | *\[Compliant / remediated / exception raised\]* | *\[Notes\]* |

## Known Tenable limitations & false positives

| Control ID | Limitation / false-positive scenario | Impact | Workaround |
|---|---|---|---|
| *\[MYSQL-DOMAIN-NNN\]* | *\[What the audit gets wrong\]* | *\[Missed FAIL / false FAIL\]* | *\[Manual step or audit tailoring\]* |

## Page change log

| Version | Date | Author | Change | Approved by |
|---|---|---|---|---|
| 0.1 | YYYY-MM-DD | *\[Name\]* | Initial draft | *\[Name\]* |
| *\[x.y\]* | YYYY-MM-DD | *\[Name\]* | *\[What changed\]* | *\[Name\]* |

---

# DB Security – MongoDB

| Property | Value |
|---|---|
| **Platform** | MongoDB |
| **Product** | MongoDB Community / Enterprise Server (replica sets, sharded clusters) |
| **Versions in scope** | *\[e.g., 7.0, 8.0\]* |
| **Policy** | `SEC-POL-DB-001` |
| **Technical basis** | CIS MongoDB 7 / 8 Benchmark |
| **Tenable audit file(s)** | CIS\_MongoDB\_\*.audit (database and mongod.conf checks via Unix audit) |
| **Tenable credential** | Database credential, type MongoDB, plus SSH credential for mongod.conf and file checks |
| **Control prefix** | `MONGO` |
| **Instances in scope** | *\[count or link to CMDB\]* |
| **Controls** | 11 |
| **Automated (Tenable)** | 7 of 11 |
| **Compliance % (last scan)** | 0% |
| **Open CRITICAL / HIGH** | 0 |
| **Last Tenable scan** | YYYY-MM-DD |
| **Owner team** | *\[Team\]* |
| **Next review due** | YYYY-MM-DD |

> **Company policy – SEC-POL-DB-001**
>
> This page is part of the company Database Security Configuration Policy (SEC-POL-DB-001). Its requirements are mandatory for every database in scope. Deviations need an approved entry in the DB Security – Exceptions Register. CIS Benchmarks and Tenable audit files are the technical basis and assessment method; where this policy differs from CIS, this policy applies.

## Scope & applicability

- Apply to every mongod and mongos, including arbiters and config servers.
- MongoDB Atlas: controls Atlas enforces (TLS, authentication) are N/A; project-level settings are reviewed manually.
- Audit logging and native encryption at rest need Enterprise; Community deployments use the compensating controls in Comments.

## Tenable assessment setup

| Item | Value |
|---|---|
| **Scan template** | Policy Compliance Auditing (credentialed) |
| **Audit file(s)** | CIS\_MongoDB\_\*.audit (database and mongod.conf checks via Unix audit) |
| **Credential** | Database credential, type MongoDB, plus SSH credential for mongod.conf and file checks |
| **Scan account privileges** | Built-in `clusterMonitor` and `read` on `admin`; no root or userAdmin roles |
| **Tailoring** | Company values from the register below override CIS defaults in the tailored audit file. Store it in *\[repository / Tenable policy name\]* |

## Control register

> **How to maintain this register**
>
> - One row per control. Control IDs are never renumbered or reused.
> - **Tenable Check** describes what the audit item reads and its pass condition. Copy the CIS section from the audit item's `reference` field into **CIS Reference**.
> - Changing a Compliant Value is a policy change: record it in the change log and get approval.
> - After every scan, update Compliance % and Open CRITICAL / HIGH in the table at the top of the page.

| Control ID | Control Name | Domain | Requirement | Severity | Compliant Value | Tenable Check (Audit / Query) | CIS Reference | Assessment | Last Review (Date / By) | Comments |
|---|---|---|---|---|---|---|---|---|---|---|
| **MONGO-VER-001** | Supported release with patches | `VER` | The server runs a MongoDB release that is not past end of life, at the latest patch level within the patch SLA. | CRITICAL | `db.version()` in the approved version list | `buildInfo` | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* |   |
| **MONGO-AAA-001** | Authorization enabled | `AAA` | Access control is on for every node. No node accepts unauthenticated connections. | CRITICAL | `security.authorization: enabled` | Unix audit: `mongod.conf`; database check: unauthenticated `listDatabases` fails | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MONGO-AAA-002** | Strong authentication mechanism | `AAA` | Users authenticate with SCRAM-SHA-256, x.509, LDAP or Kerberos. SCRAM-SHA-1 is not allowed. | HIGH | `setParameter.authenticationMechanisms` excludes `SCRAM-SHA-1` | `getParameter: authenticationMechanisms` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MONGO-AAA-003** | Cluster member authentication | `AAA` | Replica set and shard members authenticate each other with x.509 certificates (keyFile only with an exception). | HIGH | `security.clusterAuthMode: x509` | Unix audit: `mongod.conf` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MONGO-PRIV-001** | Least-privilege roles | `PRIV` | root, userAdminAnyDatabase, dbOwner and clusterAdmin are granted only to approved administrators; applications use custom least-privilege roles. | HIGH | Holders of the listed roles match the approved list | `db.getSiblingDB('admin').system.users.find()` role listing | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* | The reviewer compares role holders with the approved list. |
| **MONGO-NET-001** | Bind to required interfaces only | `NET` | mongod listens only on localhost and the interfaces applications need. | CRITICAL | `net.bindIp` does not contain `0.0.0.0` or `::`; `net.bindIpAll` not true | Unix audit: `mongod.conf` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MONGO-CRYPTO-001** | TLS required | `CRYPTO` | All client and intra-cluster connections use TLS 1.2 or higher. | HIGH | `net.tls.mode: requireTLS`; `net.tls.disabledProtocols: TLS1_0,TLS1_1` | Unix audit: `mongod.conf` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MONGO-CRYPTO-002** | Encryption at rest | `CRYPTO` | Databases classified Confidential or higher are encrypted at rest with keys held in KMIP / KMS. | HIGH | `security.enableEncryption: true` with KMIP (Enterprise), or encrypted volumes (Community) | Unix audit: `mongod.conf` | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* | Volume encryption is checked by the OS / storage team. |
| **MONGO-SVC-001** | Server-side JavaScript disabled | `SVC` | Server-side JavaScript ($where, mapReduce JS, $function) is disabled unless an application needs it. | MEDIUM | `security.javascriptEnabled: false` | Unix audit: `mongod.conf` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **MONGO-LOG-001** | Audit and system logging | `LOG` | Authentication, authorization failures and user / role changes are audited and the logs are forwarded to the SIEM. | HIGH | `auditLog.destination` set (Enterprise / Percona); `systemLog.logAppend: true` | Unix audit: `mongod.conf` | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* | Community: forward systemLog to the SIEM and record an exception for missing audit events. |
| **MONGO-OS-001** | Dedicated service account and file permissions | `OS` | mongod runs as a dedicated non-root account; keyFile and certificate keys are mode 600; dbPath is owned by the service account. | MEDIUM | Process owner `mongod`; keyFile / PEM mode 600; dbPath mode 750 or stricter | Unix audit: process owner and file permission checks | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| *\[MONGO-DOMAIN-NNN\]* | *\[Short control name\]* | *\[Domain\]* | *\[What must be true\]* | *\[CRITICAL / HIGH / MEDIUM / LOW\]* | *\[Value that passes\]* | *\[Audit item / query + pass condition\]* | *\[CIS §\]* | *\[AUTOMATED / PARTIAL / MANUAL / PLANNED / NOT FEASIBLE\]* | *\[YYYY-MM-DD / Name\]* | *\[Caveats, exception IDs\]* |

## Control details

Optional. Copy this expand for each control that needs more detail than the register holds.

### MONGO-VER-001 – Supported release with patches – details (example)

| Field | Value |
|---|---|
| **Applies to** | *\[All instances / production only / CDB only / ...\]* |
| **Rationale / risk** | *\[Why the control exists; what happens if it is not met\]* |
| **Tenable audit item** | *\[Description string of the check in the .audit file\]* |
| **Audit file and version** | *\[File name, version, date\]* |
| **Check type** | *\[SQL query / config file / registry / manual\]* |
| **Pass condition** | *\[Exact condition\]* |
| **Not applicable when** | *\[e.g., feature not installed or not licensed\]* |
| **Remediation impact** | *\[None / restart required / application change\]* |
| **CIS reference** | *\[Benchmark name, version, section\]* |
| **Exceptions** | *\[EXC-IDs, or None\]* |

**Evidence query (example, verify before use):**

```
db.adminCommand({ getCmdLineOpts: 1 }).parsed.security
db.adminCommand({ getParameter: 1, authenticationMechanisms: 1 })
```

**Remediation (example, apply through change management):**

```
# /etc/mongod.conf
security:
  authorization: enabled
  javascriptEnabled: false
net:
  bindIp: 127.0.0.1,10.20.30.40
  tls:
    mode: requireTLS
    disabledProtocols: TLS1_0,TLS1_1
```

**Review history**

| Date | Reviewed by | Outcome | Notes |
|---|---|---|---|
| YYYY-MM-DD | *\[Name\]* | *\[Compliant / remediated / exception raised\]* | *\[Notes\]* |

## Known Tenable limitations & false positives

| Control ID | Limitation / false-positive scenario | Impact | Workaround |
|---|---|---|---|
| *\[MONGO-DOMAIN-NNN\]* | *\[What the audit gets wrong\]* | *\[Missed FAIL / false FAIL\]* | *\[Manual step or audit tailoring\]* |

## Page change log

| Version | Date | Author | Change | Approved by |
|---|---|---|---|---|
| 0.1 | YYYY-MM-DD | *\[Name\]* | Initial draft | *\[Name\]* |
| *\[x.y\]* | YYYY-MM-DD | *\[Name\]* | *\[What changed\]* | *\[Name\]* |

---

# DB Security – IBM Db2

| Property | Value |
|---|---|
| **Platform** | IBM Db2 |
| **Product** | IBM Db2 for Linux, UNIX and Windows (LUW), including HADR |
| **Versions in scope** | *\[e.g., 11.5.x\]* |
| **Policy** | `SEC-POL-DB-001` |
| **Technical basis** | CIS IBM Db2 11 Benchmark |
| **Tenable audit file(s)** | CIS\_IBM\_DB2\_11\_\*.audit (database checks) + Unix audit for instance file permissions |
| **Tenable credential** | Database credential, type DB2 (database name and port; one entry per database) |
| **Control prefix** | `DB2` |
| **Instances in scope** | *\[count or link to CMDB\]* |
| **Controls** | 11 |
| **Automated (Tenable)** | 7 of 11 |
| **Compliance % (last scan)** | 0% |
| **Open CRITICAL / HIGH** | 0 |
| **Last Tenable scan** | YYYY-MM-DD |
| **Owner team** | *\[Team\]* |
| **Next review due** | YYYY-MM-DD |

> **Company policy – SEC-POL-DB-001**
>
> This page is part of the company Database Security Configuration Policy (SEC-POL-DB-001). Its requirements are mandatory for every database in scope. Deviations need an approved entry in the DB Security – Exceptions Register. CIS Benchmarks and Tenable audit files are the technical basis and assessment method; where this policy differs from CIS, this policy applies.

## Scope & applicability

- Instance (DBM CFG) controls apply once per instance; database (DB CFG) controls apply to every database in the instance.
- Db2 for z/OS and Db2 for i are out of scope of this page.

## Tenable assessment setup

| Item | Value |
|---|---|
| **Scan template** | Policy Compliance Auditing (credentialed) |
| **Audit file(s)** | CIS\_IBM\_DB2\_11\_\*.audit (database checks) + Unix audit for instance file permissions |
| **Credential** | Database credential, type DB2 (database name and port; one entry per database) |
| **Scan account privileges** | `CONNECT` on each database, `SELECT` on `SYSCAT` views, SYSMON authority; no SYSADM / DBADM |
| **Tailoring** | Company values from the register below override CIS defaults in the tailored audit file. Store it in *\[repository / Tenable policy name\]* |

## Control register

> **How to maintain this register**
>
> - One row per control. Control IDs are never renumbered or reused.
> - **Tenable Check** describes what the audit item reads and its pass condition. Copy the CIS section from the audit item's `reference` field into **CIS Reference**.
> - Changing a Compliant Value is a policy change: record it in the change log and get approval.
> - After every scan, update Compliance % and Open CRITICAL / HIGH in the table at the top of the page.

| Control ID | Control Name | Domain | Requirement | Severity | Compliant Value | Tenable Check (Audit / Query) | CIS Reference | Assessment | Last Review (Date / By) | Comments |
|---|---|---|---|---|---|---|---|---|---|---|
| **DB2-VER-001** | Supported release with current fix pack | `VER` | The instance runs a supported Db2 release at the latest mod pack / fix pack within the patch SLA. | CRITICAL | `db2level` in the approved version list | `SELECT * FROM SYSIBMADM.ENV_INST_INFO` | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* |   |
| **DB2-AAA-001** | Server-side authentication | `AAA` | The instance authenticates users on the server with encrypted credentials and does not trust client authentication. | CRITICAL | `AUTHENTICATION = SERVER_ENCRYPT` (or KERBEROS / GSSPLUGIN); `TRUST_ALLCLNTS = NO`; `TRUST_CLNTAUTH = SERVER` | Query `SYSIBMADM.DBMCFG` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **DB2-AAA-002** | Dedicated authority groups | `AAA` | SYSADM, SYSCTRL, SYSMAINT and SYSMON authorities map to dedicated OS groups with approved members. | HIGH | `SYSADM_GROUP`, `SYSCTRL_GROUP`, `SYSMAINT_GROUP`, `SYSMON_GROUP` set to dedicated groups | Query `SYSIBMADM.DBMCFG`; group membership via Unix audit | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* |   |
| **DB2-PRIV-001** | PUBLIC privileges revoked | `PRIV` | PUBLIC holds no database authorities; databases are created RESTRICTIVE or the defaults are revoked. | HIGH | No `CONNECTAUTH`, `CREATETABAUTH`, `BINDADDAUTH`, `IMPLSCHEMAAUTH` for PUBLIC in `SYSCAT.DBAUTH` | Query `SYSCAT.DBAUTH WHERE GRANTEE = 'PUBLIC'` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **DB2-PRIV-002** | Separation of duties for SECADM | `PRIV` | SECADM is held by a security administrator who does not hold DBADM or DATAACCESS. | HIGH | No grantee holds SECADM together with DBADM or DATAACCESS | Query `SYSCAT.DBAUTH` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **DB2-PRIV-003** | Catalog access restricted | `PRIV` | SELECT on the system catalog is not granted to PUBLIC where applications do not need it. | MEDIUM | No PUBLIC SELECT on `SYSCAT.*` / `SYSIBM.*` (RESTRICT\_ACCESS = YES) | Query `SYSCAT.TABAUTH` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **DB2-CRYPTO-001** | TLS-only communication | `CRYPTO` | Clients connect over TLS 1.2 or higher; plaintext TCP/IP is disabled. | HIGH | `DB2COMM = SSL`; `SSL_VERSIONS = TLSV12,TLSV13`; `SSL_SVR_KEYDB` set | Query `SYSIBMADM.DBMCFG`; `db2set -all` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **DB2-CRYPTO-002** | Native encryption at rest | `CRYPTO` | Databases classified Confidential or higher use Db2 native encryption with a keystore (PKCS#12 or KMIP). | HIGH | `ENCRYPTED = YES` in `SYSPROC.ADMIN_GET_ENCRYPTION_INFO` | `SELECT * FROM TABLE(SYSPROC.ADMIN_GET_ENCRYPTION_INFO())` | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* | Data classification comes from the CMDB. |
| **DB2-LOG-001** | db2audit configured | `LOG` | The instance audit facility records security-relevant categories and is archived to the SIEM. | HIGH | `AUDIT`, `CHECKING`, `OBJMAINT`, `SECMAINT`, `SYSADMIN`, `VALIDATE` = BOTH; database audit policy assigned | `db2audit describe` via Unix audit; `SYSCAT.AUDITPOLICIES` | *\[CIS § from .audit\]* | PARTIAL | *\[YYYY-MM-DD / Name\]* |   |
| **DB2-NET-001** | Discovery disabled | `NET` | The instance and databases cannot be discovered by DB2 discovery requests. | MEDIUM | `DISCOVER = DISABLE`; `DISCOVER_INST = DISABLE`; `DISCOVER_DB = DISABLE` | Query `SYSIBMADM.DBMCFG` / `SYSIBMADM.DBCFG` | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| **DB2-OS-001** | Instance owner and file permissions | `OS` | The instance runs under a dedicated non-root owner; the instance home and sqllib directories are not writable by others. | MEDIUM | Instance owner ≠ root; `sqllib` and database paths mode 750 or stricter | Unix audit: file permission checks | *\[CIS § from .audit\]* | AUTOMATED | *\[YYYY-MM-DD / Name\]* |   |
| *\[DB2-DOMAIN-NNN\]* | *\[Short control name\]* | *\[Domain\]* | *\[What must be true\]* | *\[CRITICAL / HIGH / MEDIUM / LOW\]* | *\[Value that passes\]* | *\[Audit item / query + pass condition\]* | *\[CIS §\]* | *\[AUTOMATED / PARTIAL / MANUAL / PLANNED / NOT FEASIBLE\]* | *\[YYYY-MM-DD / Name\]* | *\[Caveats, exception IDs\]* |

## Control details

Optional. Copy this expand for each control that needs more detail than the register holds.

### DB2-VER-001 – Supported release with current fix pack – details (example)

| Field | Value |
|---|---|
| **Applies to** | *\[All instances / production only / CDB only / ...\]* |
| **Rationale / risk** | *\[Why the control exists; what happens if it is not met\]* |
| **Tenable audit item** | *\[Description string of the check in the .audit file\]* |
| **Audit file and version** | *\[File name, version, date\]* |
| **Check type** | *\[SQL query / config file / registry / manual\]* |
| **Pass condition** | *\[Exact condition\]* |
| **Not applicable when** | *\[e.g., feature not installed or not licensed\]* |
| **Remediation impact** | *\[None / restart required / application change\]* |
| **CIS reference** | *\[Benchmark name, version, section\]* |
| **Exceptions** | *\[EXC-IDs, or None\]* |

**Evidence query (example, verify before use):**

```
SELECT NAME, VALUE FROM SYSIBMADM.DBMCFG
 WHERE NAME IN ('authentication', 'trust_allclnts', 'trust_clntauth', 'discover');
```

**Remediation (example, apply through change management):**

```
db2 update dbm cfg using AUTHENTICATION SERVER_ENCRYPT TRUST_ALLCLNTS NO TRUST_CLNTAUTH SERVER
db2stop
db2start
```

**Review history**

| Date | Reviewed by | Outcome | Notes |
|---|---|---|---|
| YYYY-MM-DD | *\[Name\]* | *\[Compliant / remediated / exception raised\]* | *\[Notes\]* |

## Known Tenable limitations & false positives

| Control ID | Limitation / false-positive scenario | Impact | Workaround |
|---|---|---|---|
| *\[DB2-DOMAIN-NNN\]* | *\[What the audit gets wrong\]* | *\[Missed FAIL / false FAIL\]* | *\[Manual step or audit tailoring\]* |

## Page change log

| Version | Date | Author | Change | Approved by |
|---|---|---|---|---|
| 0.1 | YYYY-MM-DD | *\[Name\]* | Initial draft | *\[Name\]* |
| *\[x.y\]* | YYYY-MM-DD | *\[Name\]* | *\[What changed\]* | *\[Name\]* |

---

# DB Security – Teradata

| Property | Value |
|---|---|
| **Platform** | Teradata |
| **Product** | Teradata Vantage (on-premises / VantageCore, VantageCloud Enterprise) |
| **Versions in scope** | *\[e.g., 17.20, 20.00\]* |
| **Policy** | `SEC-POL-DB-001` |
| **Technical basis** | No CIS Benchmark is published. Company baseline derived from the Teradata Vantage Security Administration guide and DB-COM controls |
| **Tenable audit file(s)** | No Tenable database audit for Teradata. Planned: custom Unix audit running BTEQ queries on a TPA node (cmd\_exec) |
| **Tenable credential** | SSH credential to a TPA node for the custom audit; until then MANUAL review |
| **Control prefix** | `TD` |
| **Instances in scope** | *\[count or link to CMDB\]* |
| **Controls** | 10 |
| **Automated (Tenable)** | 0 of 10 |
| **Compliance % (last scan)** | 0% |
| **Open CRITICAL / HIGH** | 0 |
| **Last Tenable scan** | YYYY-MM-DD |
| **Owner team** | *\[Team\]* |
| **Next review due** | YYYY-MM-DD |

> **Company policy – SEC-POL-DB-001**
>
> This page is part of the company Database Security Configuration Policy (SEC-POL-DB-001). Its requirements are mandatory for every database in scope. Deviations need an approved entry in the DB Security – Exceptions Register. CIS Benchmarks and Tenable audit files are the technical basis and assessment method; where this policy differs from CIS, this policy applies.

## Scope & applicability

- **No CIS Benchmark and no native Tenable database checks.** Every control on this page is reviewed MANUALLY until the custom audit is built (see the Automation status in each row).
- Node OS (SLES) hardening follows the company Linux standard and is scanned by the Tenable Unix audit.
- VantageCloud Lake: controls the provider manages are N/A.

## Tenable assessment setup

| Item | Value |
|---|---|
| **Scan template** | Policy Compliance Auditing (credentialed) |
| **Audit file(s)** | No Tenable database audit for Teradata. Planned: custom Unix audit running BTEQ queries on a TPA node (cmd\_exec) |
| **Credential** | SSH credential to a TPA node for the custom audit; until then MANUAL review |
| **Scan account privileges** | `SELECT` on the `DBC` dictionary views listed below; no DBC or security administrator rights |
| **Tailoring** | Company values from the register below override CIS defaults in the tailored audit file. Store it in *\[repository / Tenable policy name\]* |

## Control register

> **How to maintain this register**
>
> - One row per control. Control IDs are never renumbered or reused.
> - **Tenable Check** describes what the audit item reads and its pass condition. Copy the CIS section from the audit item's `reference` field into **CIS Reference**.
> - Changing a Compliant Value is a policy change: record it in the change log and get approval.
> - After every scan, update Compliance % and Open CRITICAL / HIGH in the table at the top of the page.

| Control ID | Control Name | Domain | Requirement | Severity | Compliant Value | Tenable Check (Audit / Query) | CIS Reference | Assessment | Last Review (Date / By) | Comments |
|---|---|---|---|---|---|---|---|---|---|---|
| **TD-VER-001** | Supported release with current PUT / patches | `VER` | The system runs a supported Vantage release and current efixes within the patch SLA. | CRITICAL | `SELECT InfoData FROM DBC.DBCInfoV` in the approved version list | Manual: query `DBC.DBCInfoV` | *\[CIS § from .audit\]* | MANUAL | *\[YYYY-MM-DD / Name\]* |   |
| **TD-AAA-001** | DBC user protected | `AAA` | The DBC user is not used for daily administration, has a vaulted password, and can log on only from approved hosts. | CRITICAL | DBC password in PAM; logon rules limit DBC to approved hosts; no direct DBC sessions in `DBC.LogOnOffV` outside break-glass | Manual: `DBC.LogonRulesV` and `DBC.LogOnOffV` | *\[CIS § from .audit\]* | MANUAL | *\[YYYY-MM-DD / Name\]* |   |
| **TD-AAA-002** | System password and lockout defaults | `AAA` | System-wide password defaults meet the corporate password standard. | HIGH | `PasswordMinChar` ≥ 14, digits and special characters required, `MaxLogonAttempts` ≤ 5, `LockedUserExpire` ≥ 30 min, `ExpirePassword` ≤ 90 days, `PasswordReuse` ≥ 365 days | Manual: `SELECT * FROM DBC.SysSecDefaults` | *\[CIS § from .audit\]* | PLANNED | *\[YYYY-MM-DD / Name\]* |   |
| **TD-AAA-003** | Central authentication | `AAA` | Human users authenticate through LDAP / Kerberos (TDGSS). TD2 (database) authentication is limited to service and break-glass accounts. | HIGH | Default mechanism LDAP or KRB5 in TDGSS config; TD2 users listed and approved | Manual: TDGSS configuration on the TPA node | *\[CIS § from .audit\]* | MANUAL | *\[YYYY-MM-DD / Name\]* |   |
| **TD-PRIV-001** | Role-based access, no PUBLIC grants | `PRIV` | Access is granted through roles. Nothing is granted to PUBLIC or ALL beyond defaults, and WITH GRANT OPTION is limited to administrators. | HIGH | No user-level grants outside admin accounts in `DBC.AllRightsV`; no `GrantAuthority = 'Y'` to non-admins | Manual: `DBC.AllRightsV`, `DBC.AllRoleRightsV` | *\[CIS § from .audit\]* | PLANNED | *\[YYYY-MM-DD / Name\]* |   |
| **TD-PRIV-002** | Dictionary access restricted | `PRIV` | Users see only the dictionary rows about objects they can access (X views), and direct access to DBC tables is revoked from PUBLIC. | MEDIUM | Applications use `DBC.*VX` views; PUBLIC SELECT on DBC tables revoked | Manual: `DBC.AllRightsV WHERE UserName = 'PUBLIC'` | *\[CIS § from .audit\]* | MANUAL | *\[YYYY-MM-DD / Name\]* |   |
| **TD-CRYPTO-001** | Encryption in transit | `CRYPTO` | Client connections are encrypted with TLS (Vantage 17.10+) or TDGSS confidentiality. | HIGH | TLS enabled on the gateway with TLS 1.2+, or TDGSS `ConfidentialityRequired` = yes (AES-256) | Manual: gateway (`gtwcontrol`) and TDGSS configuration | *\[CIS § from .audit\]* | MANUAL | *\[YYYY-MM-DD / Name\]* |   |
| **TD-CRYPTO-002** | Encryption at rest | `CRYPTO` | Systems holding Confidential data use self-encrypting drives or Vantage storage encryption; backups are encrypted. | HIGH | SED / storage encryption enabled; backup encryption enabled in DSA / BAR | Manual: platform evidence from Teradata support | *\[CIS § from .audit\]* | NOT FEASIBLE | *\[YYYY-MM-DD / Name\]* | Not visible from SQL; evidence collected annually. |
| **TD-LOG-001** | Access logging and DBQL | `LOG` | Logons, failed logons, grants / revokes and access to sensitive objects are logged; DBQL is enabled; logs are forwarded to the SIEM. | HIGH | Access logging rules in `DBC.AccLogRulesV` for GRANT, REVOKE, CREATE / DROP USER; DBQL active in `DBC.DBQLRulesV` | Manual: `DBC.AccLogRulesV`, `DBC.DBQLRulesV` | *\[CIS § from .audit\]* | PLANNED | *\[YYYY-MM-DD / Name\]* |   |
| **TD-NET-001** | Logon rules restrict client hosts | `NET` | Logon rules allow each privileged user only from approved client hosts. | MEDIUM | `GRANT LOGON ON <host> TO <user>` rules present for privileged users | Manual: `DBC.LogonRulesV` | *\[CIS § from .audit\]* | MANUAL | *\[YYYY-MM-DD / Name\]* |   |
| *\[TD-DOMAIN-NNN\]* | *\[Short control name\]* | *\[Domain\]* | *\[What must be true\]* | *\[CRITICAL / HIGH / MEDIUM / LOW\]* | *\[Value that passes\]* | *\[Audit item / query + pass condition\]* | *\[CIS §\]* | *\[AUTOMATED / PARTIAL / MANUAL / PLANNED / NOT FEASIBLE\]* | *\[YYYY-MM-DD / Name\]* | *\[Caveats, exception IDs\]* |

## Control details

Optional. Copy this expand for each control that needs more detail than the register holds.

### TD-VER-001 – Supported release with current PUT / patches – details (example)

| Field | Value |
|---|---|
| **Applies to** | *\[All instances / production only / CDB only / ...\]* |
| **Rationale / risk** | *\[Why the control exists; what happens if it is not met\]* |
| **Tenable audit item** | *\[Description string of the check in the .audit file\]* |
| **Audit file and version** | *\[File name, version, date\]* |
| **Check type** | *\[SQL query / config file / registry / manual\]* |
| **Pass condition** | *\[Exact condition\]* |
| **Not applicable when** | *\[e.g., feature not installed or not licensed\]* |
| **Remediation impact** | *\[None / restart required / application change\]* |
| **CIS reference** | *\[Benchmark name, version, section\]* |
| **Exceptions** | *\[EXC-IDs, or None\]* |

**Evidence query (example, verify before use):**

```
SELECT PasswordMinChar, PasswordDigits, PasswordSpecChar,
       MaxLogonAttempts, LockedUserExpire, ExpirePassword, PasswordReuse
  FROM DBC.SysSecDefaults;
```

**Remediation (example, apply through change management):**

```
UPDATE DBC.SysSecDefaults
   SET PasswordMinChar = 14, MaxLogonAttempts = 5, ExpirePassword = 90, PasswordReuse = 365;
-- takes effect after the next system restart or tpareset; follow the change process
```

**Review history**

| Date | Reviewed by | Outcome | Notes |
|---|---|---|---|
| YYYY-MM-DD | *\[Name\]* | *\[Compliant / remediated / exception raised\]* | *\[Notes\]* |

## Known Tenable limitations & false positives

| Control ID | Limitation / false-positive scenario | Impact | Workaround |
|---|---|---|---|
| *\[TD-DOMAIN-NNN\]* | *\[What the audit gets wrong\]* | *\[Missed FAIL / false FAIL\]* | *\[Manual step or audit tailoring\]* |

## Page change log

| Version | Date | Author | Change | Approved by |
|---|---|---|---|---|
| 0.1 | YYYY-MM-DD | *\[Name\]* | Initial draft | *\[Name\]* |
| *\[x.y\]* | YYYY-MM-DD | *\[Name\]* | *\[What changed\]* | *\[Name\]* |

---

# DB Security – Exceptions Register

> **Company policy – SEC-POL-DB-001**
>
> This page is part of the company Database Security Configuration Policy (SEC-POL-DB-001). Its requirements are mandatory for every database in scope. Deviations need an approved entry in the DB Security – Exceptions Register. CIS Benchmarks and Tenable audit files are the technical basis and assessment method; where this policy differs from CIS, this policy applies.

> **Before you add an exception**
>
> - Every exception needs a business justification, a compensating control, a named risk owner and an expiry date (max. 12 months).
> - CRITICAL controls: approval by the policy owner (CISO). Others: Head of Database Engineering and the application owner.
> - Ask Vulnerability Management to exclude the instance from that Tenable audit item, and record it in **Excluded in Tenable?**.
> - Put the Exception ID in the Comments column of the control on its platform page.

## Status

| Status | Meaning |
|---|---|
| ACTIVE | Approved and within its expiry date |
| EXPIRING | Expires within 30 days; renew or remediate |
| EXPIRED | Past expiry; the instance is non-compliant |
| CLOSED | Remediated or no longer needed |

## Register

| Exception ID | Control ID | Platform | Instances / databases | Business justification | Compensating control | Risk owner | Approved by / on | Expires on | Excluded in Tenable? | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| **DBEXC-001** | *\[MSSQL-SVC-002\]* | *\[Microsoft SQL Server\]* | *\[Instance names / CMDB IDs\]* | *\[e.g., Database Mail needed for application alerts\]* | *\[e.g., SMTP relay restricted to internal domain\]* | *\[Name, role\]* | *\[Name / YYYY-MM-DD\]* | YYYY-MM-DD | *\[Yes / No\]* | ACTIVE |
