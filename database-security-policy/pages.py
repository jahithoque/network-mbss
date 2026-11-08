"""Content model for the Database Security Configuration Policy Confluence pages.

Same block model as ../confluence-template/pages.py: build.py renders the
blocks to Confluence storage format, wiki markup, Markdown and the preview kit.
Edit content here, then run `python3 build.py`.

Block types
  ("h", level, text)
  ("p", inlines)
  ("ul", [inlines, ...])
  ("panel", kind, title, blocks)          kind: info | note | tip | warning
  ("toc", max_level)
  ("props", macro_id, [(key, inlines)])   Page Properties macro
  ("report", cql, headings)               Page Properties Report macro
  ("table", headers, rows)                rows: [[inlines, ...], ...]
  ("expand", title, blocks)
  ("code", text)
  ("alt", macro_blocks, paste_blocks)     macro_blocks go to storage / wiki,
                                          paste_blocks to the copy-paste HTML

Inlines are a string or a list of: str, ("b", s), ("i", s), ("code", s),
("st", colour, title) status lozenge, ("ph", s) placeholder, ("br",).

The controls are the company's own requirements. CIS Benchmarks and the
Tenable audit files built from them are the technical basis and the
assessment method; CIS section numbers are left as placeholders to be filled
from the `reference` field of the Tenable audit file version in use, because
they change between benchmark releases.
"""

POLICY_ID = "SEC-POL-DB-001"
POLICY_TITLE = "Database Security Configuration Policy"

# ---------------------------------------------------------------- legends

SEVERITY = {"CRITICAL": "Red", "HIGH": "Yellow", "MEDIUM": "Blue", "LOW": "Grey"}

ASSESSMENT = {
    "AUTOMATED": "Green",
    "PARTIAL": "Yellow",
    "MANUAL": "Blue",
    "PLANNED": "Purple",
    "NOT FEASIBLE": "Grey",
}


def sev(name):
    return ("st", SEVERITY[name], name)


def asm(name):
    return ("st", ASSESSMENT[name], name)


def ph(text):
    return [("ph", text)]


def c(s):
    return ("code", s)


CONTROL_COLUMNS = [
    "Control ID",
    "Control Name",
    "Domain",
    "Requirement",
    "Severity",
    "Compliant Value",
    "Tenable Check (Audit / Query)",
    "CIS Reference",
    "Assessment",
    "Last Review (Date / By)",
    "Comments",
]

DOMAINS = [
    ("VER", "Software & patching", "Vendor-supported release, security patches / release updates applied"),
    ("AAA", "Authentication", "Default accounts, password policy, lockout, central authentication"),
    ("PRIV", "Authorization & privileges", "Least privilege, PUBLIC / guest rights, admin role membership"),
    ("CRYPTO", "Encryption", "TLS in transit, encryption at rest, key management"),
    ("LOG", "Auditing & logging", "Database audit trail, failed / successful logons, forwarding to SIEM"),
    ("NET", "Network exposure", "Listener / bind address, ports, remote administration"),
    ("SVC", "Features & configuration", "Dangerous features disabled, sample databases removed, secure parameters"),
    ("OS", "Host & file system", "Service account, file permissions, no clear-text credentials on disk"),
    ("BKP", "Backup & recovery", "Encrypted backups, restore testing"),
]

# Company-wide values every platform page must meet (or be stricter than).
COMMON_BASELINE = [
    ["DB-COM-01", "VER", "Run a vendor-supported release and apply security patches within the patch SLA.",
     "No end-of-support versions; latest security patch level minus one at most"],
    ["DB-COM-02", "AAA", "Change, lock or remove every vendor default and sample account.",
     "No account with a default or blank password"],
    ["DB-COM-03", "AAA", "Human administrators authenticate with named accounts through central directory (AD / LDAP / Kerberos) where the platform supports it.",
     "No shared admin logons; break-glass account vaulted in PAM"],
    ["DB-COM-04", "AAA", "Local database accounts follow the corporate password standard.",
     "Min. 14 characters, complexity on, lockout after ≤ 5 failures, expiry ≤ 90 days for human accounts, reuse history ≥ 10"],
    ["DB-COM-05", "PRIV", "Grant privileges through roles on least privilege. Nothing beyond vendor defaults to PUBLIC / guest.",
     "Admin roles limited to the approved DBA group; quarterly access review"],
    ["DB-COM-06", "CRYPTO", "Encrypt all client and replication traffic.",
     "TLS 1.2 or higher (or native network encryption with AES-256); plaintext listeners disabled"],
    ["DB-COM-07", "CRYPTO", "Encrypt data at rest for databases classified Confidential or higher.",
     "TDE / native encryption, or encrypted volumes with keys outside the DB host"],
    ["DB-COM-08", "LOG", "Audit logons (success and failure), privilege and security changes, and DDL. Forward to the SIEM.",
     "Audit enabled; retained ≥ 12 months (90 days online)"],
    ["DB-COM-09", "NET", "Expose the database only to the application and admin networks that need it.",
     "Bound to required interfaces; host / network firewall allow-list"],
    ["DB-COM-10", "SVC", "Disable features that execute OS commands, read files or open network connections unless approved.",
     "Off by default; approved exceptions only"],
    ["DB-COM-11", "OS", "Run database services under a dedicated, non-root / non-administrator account. No credentials in clear text in files or scripts.",
     "Dedicated service account; config files readable only by the service account"],
    ["DB-COM-12", "BKP", "Encrypt backups and test restores.",
     "Encrypted backups; restore test at least annually"],
]


# Which platform controls implement each common baseline requirement
# (drives the cross-platform control matrix on the policy page).
BASELINE_MAP = {
    "DB-COM-01": ["ORA-VER-001", "MSSQL-VER-001", "MYSQL-VER-001", "MONGO-VER-001", "DB2-VER-001", "TD-VER-001"],
    "DB-COM-02": ["ORA-AAA-001", "ORA-SVC-002", "MSSQL-AAA-002", "MYSQL-AAA-001", "MYSQL-SVC-002", "MONGO-AAA-001", "TD-AAA-001"],
    "DB-COM-03": ["ORA-AAA-003", "ORA-AAA-004", "MSSQL-AAA-001", "MONGO-AAA-002", "MONGO-AAA-003", "DB2-AAA-001", "DB2-AAA-002", "TD-AAA-003"],
    "DB-COM-04": ["ORA-AAA-002", "MSSQL-AAA-003", "MYSQL-AAA-002", "MYSQL-AAA-003", "TD-AAA-002"],
    "DB-COM-05": ["ORA-PRIV-001", "ORA-PRIV-002", "MSSQL-PRIV-001", "MSSQL-PRIV-002", "MSSQL-PRIV-003", "MYSQL-PRIV-001",
                  "MONGO-PRIV-001", "DB2-PRIV-001", "DB2-PRIV-002", "DB2-PRIV-003", "TD-PRIV-001", "TD-PRIV-002"],
    "DB-COM-06": ["ORA-CRYPTO-001", "MSSQL-CRYPTO-001", "MYSQL-CRYPTO-001", "MONGO-CRYPTO-001", "DB2-CRYPTO-001", "TD-CRYPTO-001"],
    "DB-COM-07": ["ORA-CRYPTO-002", "MSSQL-CRYPTO-002", "MONGO-CRYPTO-002", "DB2-CRYPTO-002", "TD-CRYPTO-002"],
    "DB-COM-08": ["ORA-LOG-001", "MSSQL-LOG-001", "MYSQL-LOG-001", "MONGO-LOG-001", "DB2-LOG-001", "TD-LOG-001"],
    "DB-COM-09": ["ORA-NET-001", "MSSQL-NET-001", "MONGO-NET-001", "DB2-NET-001", "TD-NET-001"],
    "DB-COM-10": ["ORA-PRIV-001", "ORA-SVC-001", "MSSQL-SVC-001", "MSSQL-SVC-002", "MSSQL-SVC-003", "MYSQL-SVC-001",
                  "MYSQL-SVC-003", "MONGO-SVC-001"],
    "DB-COM-11": ["MSSQL-OS-001", "MYSQL-OS-001", "MYSQL-OS-002", "MONGO-OS-001", "DB2-OS-001"],
    "DB-COM-12": [],
}


def ctl(cid, name, dom, req, severity, value, check, status, comment=""):
    return {"id": cid, "name": name, "dom": dom, "req": req, "sev": severity,
            "val": value, "check": check, "status": status, "comment": comment}


# ---------------------------------------------------------------- platforms

PLATFORMS = [
    {
        "slug": "01-oracle",
        "short": "Oracle",
        "product": "Oracle Database (single instance, RAC, Data Guard; CDB and PDBs)",
        "versions": "e.g., 19c, 23ai",
        "prefix": "ORA",
        "cis": "CIS Oracle Database 19c Benchmark (use the 23ai benchmark for 23ai)",
        "audit_file": "CIS_Oracle_Database_19c_*.audit (database checks) + CIS Unix audit for listener / file checks",
        "credential": "Database credential, type Oracle (SID or service name; scan each PDB as well as the CDB)",
        "scan_account": [c("CREATE SESSION"), ", ", c("SELECT ANY DICTIONARY"), " (or ", c("SELECT_CATALOG_ROLE"),
                         "), ", c("AUDIT_VIEWER"), "; no DBA role"],
        "scope_notes": [
            ["Apply database-level controls to the CDB root and to every PDB. State in Comments if a control is CDB-only."],
            ["Listener and ", c("sqlnet.ora"), " controls are checked through the Unix (SSH) part of the scan on the database host."],
            ["Oracle Autonomous / managed cloud services: controls the provider manages are N/A; record them in Comments."],
        ],
        "controls": [
            ctl("ORA-VER-001", "Supported release with current Release Update", "VER",
                "The database runs a release under Oracle Premier or Extended Support with a Release Update no older than the previous quarterly CPU.",
                "CRITICAL", ["Latest or previous quarterly RU in ", c("DBA_REGISTRY_SQLPATCH")],
                [c("SELECT banner_full FROM v$version"), " and latest ", c("DBA_REGISTRY_SQLPATCH"), " entry; compared with the approved RU list"],
                "PARTIAL", "Tenable reports the version; the approved RU list is maintained by the DBA team."),
            ctl("ORA-AAA-001", "No default passwords", "AAA",
                "No account may use an Oracle default password. Unused Oracle-supplied accounts are locked and expired.",
                "CRITICAL", [c("SELECT * FROM dba_users_with_defpwd"), " returns no rows"],
                ["Query ", c("DBA_USERS_WITH_DEFPWD"), "; FAIL on any row"], "AUTOMATED"),
            ctl("ORA-AAA-002", "Password and lockout profile", "AAA",
                "Every profile used by a non-service account enforces the corporate password standard and a verify function.",
                "HIGH",
                [c("FAILED_LOGIN_ATTEMPTS"), " ≤ 5, ", c("PASSWORD_LOCK_TIME"), " ≥ 1, ", c("PASSWORD_LIFE_TIME"), " ≤ 90, ",
                 c("PASSWORD_REUSE_MAX"), " ≥ 10, ", c("PASSWORD_GRACE_TIME"), " ≤ 5, ", c("PASSWORD_VERIFY_FUNCTION"), " not NULL"],
                ["Query ", c("DBA_PROFILES"), " for each profile assigned in ", c("DBA_USERS")],
                "AUTOMATED", "Service accounts use a separate profile with no expiry; their passwords are rotated by PAM."),
            ctl("ORA-AAA-003", "Remote OS authentication disabled", "AAA",
                "The database must not trust the client operating system to authenticate users or roles.",
                "HIGH", [c("REMOTE_OS_AUTHENT"), " / ", c("REMOTE_OS_ROLES"), " = FALSE, ", c("OS_ROLES"), " = FALSE"],
                ["Query ", c("v$parameter")], "AUTOMATED"),
            ctl("ORA-AAA-004", "Password file restricted", "AAA",
                "Remote SYSDBA logon through a password file is allowed only where a documented need exists (e.g., Data Guard).",
                "MEDIUM", [c("REMOTE_LOGIN_PASSWORDFILE"), " = NONE, or EXCLUSIVE with an approved exception"],
                ["Query ", c("v$parameter")], "AUTOMATED"),
            ctl("ORA-PRIV-001", "No PUBLIC execute on network and file packages", "PRIV",
                "PUBLIC must not have EXECUTE on packages that read files, open network connections or run dynamic SQL / Java.",
                "HIGH", ["No PUBLIC grant on ", c("UTL_FILE"), ", ", c("UTL_TCP"), ", ", c("UTL_HTTP"), ", ", c("UTL_SMTP"),
                         ", ", c("UTL_INADDR"), ", ", c("DBMS_JAVA"), ", ", c("DBMS_SCHEDULER"), ", ", c("DBMS_LOB")],
                ["Query ", c("DBA_TAB_PRIVS WHERE grantee='PUBLIC'"), " for the package list"], "AUTOMATED"),
            ctl("ORA-PRIV-002", "Powerful privileges restricted", "PRIV",
                "*ANY* system privileges, DBA, and administrative privileges (SYSDBA, SYSOPER, SYSBACKUP…) are granted only to approved accounts.",
                "HIGH", ["Grantees in ", c("DBA_SYS_PRIVS"), " / ", c("DBA_ROLE_PRIVS"), " / ", c("v$pwfile_users"), " match the approved list"],
                ["Tenable lists grantees; reviewer compares with the approved list"],
                "PARTIAL", "Tenable cannot know the approved list; record the review outcome here."),
            ctl("ORA-SVC-001", "Security initialization parameters", "SVC",
                "Security-related initialization parameters are set to the company values.",
                "MEDIUM", [c("SEC_MAX_FAILED_LOGIN_ATTEMPTS"), " ≤ 3, ", c("SEC_PROTOCOL_ERROR_FURTHER_ACTION"), " = (DROP,3), ",
                           c("SEC_RETURN_SERVER_RELEASE_BANNER"), " = FALSE, ", c("SQL92_SECURITY"), " = TRUE, ",
                           c("_TRACE_FILES_PUBLIC"), " = FALSE, ", c("RESOURCE_LIMIT"), " = TRUE"],
                ["Query ", c("v$parameter"), " / ", c("x$ksppcv"), " for hidden parameters"], "AUTOMATED"),
            ctl("ORA-SVC-002", "Sample schemas removed", "SVC",
                "Sample schemas (HR, OE, SH, PM, IX, BI, SCOTT) are not installed in production databases.",
                "LOW", ["No sample schema in ", c("DBA_USERS")], ["Query ", c("DBA_USERS")], "AUTOMATED"),
            ctl("ORA-NET-001", "Listener hardened", "NET",
                "The listener cannot be reconfigured at run time and does not offer external procedures.",
                "HIGH", [c("ADMIN_RESTRICTIONS_<listener>=ON"), " in ", c("listener.ora"), "; no ", c("EXTPROC"), " entry"],
                ["Unix audit: content check on ", c("$ORACLE_HOME/network/admin/listener.ora")], "AUTOMATED"),
            ctl("ORA-CRYPTO-001", "Network encryption required", "CRYPTO",
                "All client connections are encrypted with TLS or Oracle native network encryption.",
                "HIGH", [c("SQLNET.ENCRYPTION_SERVER = REQUIRED"), ", ", c("SQLNET.ENCRYPTION_TYPES_SERVER = (AES256)"),
                         ", or TCPS only with TLS 1.2+"],
                ["Unix audit: content check on ", c("sqlnet.ora")], "AUTOMATED"),
            ctl("ORA-CRYPTO-002", "Encryption at rest (TDE)", "CRYPTO",
                "Databases classified Confidential or higher use TDE tablespace encryption with the keystore outside the data files.",
                "HIGH", ["Keystore OPEN in ", c("v$encryption_wallet"), "; user tablespaces ENCRYPTED = YES"],
                ["Query ", c("v$encryption_wallet"), " and ", c("DBA_TABLESPACES")],
                "PARTIAL", "Tenable cannot see data classification; scope comes from the CMDB."),
            ctl("ORA-LOG-001", "Unified auditing policies", "LOG",
                "Unified auditing records logons, privilege use and security-relevant changes and is forwarded to the SIEM.",
                "HIGH", ["Policies enabled in ", c("AUDIT_UNIFIED_ENABLED_POLICIES"), " cover LOGON / LOGOFF, ",
                         c("ORA_SECURECONFIG"), ", ", c("ORA_ACCOUNT_MGMT"), ", ", c("ORA_DATABASE_PARAMETER")],
                ["Query ", c("AUDIT_UNIFIED_ENABLED_POLICIES")],
                "PARTIAL", "SIEM forwarding is confirmed manually by the SOC."),
        ],
        "example_query": "SELECT username, account_status\n  FROM dba_users_with_defpwd d JOIN dba_users u USING (username);",
        "remediation": "ALTER USER <username> PASSWORD EXPIRE ACCOUNT LOCK;\n-- or set a new password if the account is required",
    },
    {
        "slug": "02-mssql",
        "short": "Microsoft SQL Server",
        "product": "Microsoft SQL Server (Database Engine, on Windows or Linux; Always On availability groups)",
        "versions": "e.g., 2019, 2022",
        "prefix": "MSSQL",
        "cis": "CIS Microsoft SQL Server 2019 / 2022 Benchmark",
        "audit_file": "CIS_Microsoft_SQL_Server_2022_*.audit (database checks) + Windows audit for registry / service checks",
        "credential": "Database credential, type SQL Server (Windows or SQL authentication; one entry per instance / port)",
        "scan_account": [c("VIEW SERVER STATE"), ", ", c("VIEW ANY DEFINITION"), ", ", c("CONNECT ANY DATABASE"),
                         " (2014+), membership of the user role in ", c("msdb"), "; no sysadmin"],
        "scope_notes": [
            ["Instance-level controls apply to every instance, including named instances and SSRS / SSAS hosts where a Database Engine is installed."],
            ["Database-level controls (guest, TRUSTWORTHY, TDE) apply to every user database; system databases are noted in Comments."],
            ["Azure SQL Database / Managed Instance: controls the platform enforces are N/A."],
        ],
        "controls": [
            ctl("MSSQL-VER-001", "Supported version with latest CU / GDR", "VER",
                "The instance runs a supported version with the latest security update (CU or GDR) within the patch SLA.",
                "CRITICAL", [c("SERVERPROPERTY('ProductUpdateLevel')"), " matches the approved build list"],
                [c("SELECT @@VERSION"), "; compared with the approved build list"], "PARTIAL",
                "Tenable vulnerability plugins also flag missing updates."),
            ctl("MSSQL-AAA-001", "Windows authentication mode", "AAA",
                "Instances use Windows Authentication only. Mixed mode needs an approved exception.",
                "HIGH", [c("SERVERPROPERTY('IsIntegratedSecurityOnly')"), " = 1"],
                ["Query ", c("SERVERPROPERTY")], "AUTOMATED"),
            ctl("MSSQL-AAA-002", "sa disabled and renamed", "AAA",
                "The built-in sa login (principal_id 1) is disabled and renamed.",
                "HIGH", [c("sys.server_principals"), " where ", c("principal_id = 1"), ": ", c("is_disabled = 1"), ", name ≠ 'sa'"],
                ["Query ", c("sys.server_principals")], "AUTOMATED"),
            ctl("MSSQL-AAA-003", "SQL logins follow password policy", "AAA",
                "Every SQL-authenticated login enforces the Windows password policy; expiration is enforced for logins in sysadmin.",
                "HIGH", [c("is_policy_checked = 1"), " for all SQL logins; ", c("is_expiration_checked = 1"), " for sysadmin members"],
                ["Query ", c("sys.sql_logins")], "AUTOMATED"),
            ctl("MSSQL-SVC-001", "xp_cmdshell disabled", "SVC",
                "xp_cmdshell must be disabled.",
                "CRITICAL", [c("xp_cmdshell"), " value_in_use = 0"], ["Query ", c("sys.configurations")], "AUTOMATED"),
            ctl("MSSQL-SVC-002", "Surface-area options disabled", "SVC",
                "Server options that extend the attack surface are disabled unless approved.",
                "HIGH", ["value_in_use = 0 for ", c("Ad Hoc Distributed Queries"), ", ", c("clr enabled"), ", ",
                         c("cross db ownership chaining"), ", ", c("Database Mail XPs"), ", ", c("Ole Automation Procedures"),
                         ", ", c("remote access"), ", ", c("scan for startup procs"), "; ", c("clr strict security"), " = 1"],
                ["Query ", c("sys.configurations")], "AUTOMATED",
                "Database Mail is often required; record approved instances as exceptions."),
            ctl("MSSQL-SVC-003", "Remote DAC restricted", "SVC",
                "The remote dedicated admin connection is off, except on clustered instances where it is needed.",
                "MEDIUM", [c("remote admin connections"), " = 0 (1 allowed on failover cluster instances)"],
                ["Query ", c("sys.configurations")], "AUTOMATED"),
            ctl("MSSQL-PRIV-001", "guest has no CONNECT in user databases", "PRIV",
                "The guest user cannot connect to any database other than master, tempdb and msdb.",
                "HIGH", ["No ", c("CONNECT"), " granted to guest in user databases"],
                ["Query ", c("sys.database_permissions"), " in each database"], "AUTOMATED"),
            ctl("MSSQL-PRIV-002", "PUBLIC role has only default permissions", "PRIV",
                "No permissions are granted to the public server role beyond the defaults; sysadmin members match the approved list.",
                "HIGH", ["Only default public grants (VIEW ANY DATABASE, CONNECT on default endpoints)"],
                ["Query ", c("sys.server_permissions"), " for grantee_principal_id = 2; list sysadmin members"],
                "PARTIAL", "sysadmin membership is compared with the approved list by the reviewer."),
            ctl("MSSQL-PRIV-003", "TRUSTWORTHY off", "PRIV",
                "TRUSTWORTHY is OFF for every user database.",
                "HIGH", [c("is_trustworthy_on = 0"), " (msdb excepted)"], ["Query ", c("sys.databases")], "AUTOMATED"),
            ctl("MSSQL-NET-001", "Instance not advertised", "NET",
                "The instance is hidden from SQL Browser enumeration and does not listen on the default port where feasible.",
                "LOW", ["HideInstance = 1; static port other than 1433"],
                ["Windows audit: registry check under ", c("MSSQLServer\\SuperSocketNetLib")], "AUTOMATED"),
            ctl("MSSQL-CRYPTO-001", "Forced TLS encryption", "CRYPTO",
                "Client connections are encrypted with TLS 1.2 or higher using a trusted certificate.",
                "HIGH", ["ForceEncryption = 1; TLS 1.0 / 1.1 disabled in SCHANNEL"],
                ["Windows audit: registry check on ", c("SuperSocketNetLib\\ForceEncryption"), " and SCHANNEL protocols"], "AUTOMATED"),
            ctl("MSSQL-CRYPTO-002", "TDE for confidential databases", "CRYPTO",
                "Databases classified Confidential or higher use Transparent Data Encryption; certificates are backed up off-host.",
                "HIGH", [c("sys.dm_database_encryption_keys"), " encryption_state = 3"],
                ["Query ", c("sys.dm_database_encryption_keys")], "PARTIAL",
                "Data classification comes from the CMDB."),
            ctl("MSSQL-LOG-001", "Login and security auditing", "LOG",
                "Failed and successful logins and security changes are audited and forwarded to the SIEM.",
                "HIGH", ["Server audit spec with ", c("FAILED_LOGIN_GROUP"), ", ", c("SUCCESSFUL_LOGIN_GROUP"), ", ",
                         c("AUDIT_CHANGE_GROUP"), "; login auditing = Both"],
                ["Query ", c("sys.server_audit_specification_details"), "; registry AuditLevel = 3"], "PARTIAL",
                "SIEM forwarding is confirmed manually by the SOC."),
            ctl("MSSQL-OS-001", "Dedicated low-privilege service accounts", "OS",
                "Each SQL Server service runs under its own virtual, managed or domain account that is not a local or domain administrator.",
                "MEDIUM", ["Service accounts not in local Administrators; one account per service"],
                [c("sys.dm_server_services"), " + Windows audit group membership check"], "PARTIAL"),
        ],
        "example_query": "SELECT name, CAST(value_in_use AS int) AS value_in_use\n  FROM sys.configurations\n WHERE name IN ('xp_cmdshell', 'clr enabled', 'Ole Automation Procedures');",
        "remediation": "EXEC sp_configure 'show advanced options', 1; RECONFIGURE;\nEXEC sp_configure 'xp_cmdshell', 0; RECONFIGURE;\nEXEC sp_configure 'show advanced options', 0; RECONFIGURE;",
    },
    {
        "slug": "03-mysql",
        "short": "MySQL",
        "product": "MySQL Community / Enterprise Server (InnoDB Cluster, replication)",
        "versions": "e.g., 8.0, 8.4 LTS",
        "prefix": "MYSQL",
        "cis": "CIS Oracle MySQL Community / Enterprise Server 8.0 Benchmark",
        "audit_file": "CIS_MySQL_8.0_*.audit (database checks) + Unix audit for my.cnf and file permission checks",
        "credential": "Database credential, type MySQL (TCP port; one entry per instance)",
        "scan_account": [c("SELECT"), " on ", c("mysql.*"), " and ", c("performance_schema.*"), ", ", c("PROCESS"),
                         "; no SUPER or administrative grants"],
        "scope_notes": [
            ["MariaDB and Percona Server are in scope with this page as the baseline; differences are noted in Comments."],
            ["Configuration-file controls (", c("my.cnf"), ") are checked through the Unix (SSH) part of the scan."],
            ["Managed services (Amazon RDS / Aurora, Azure Database for MySQL): host and file controls are N/A."],
        ],
        "controls": [
            ctl("MYSQL-VER-001", "Supported release with security patches", "VER",
                "The server runs a supported release (8.0 until its EOL, or 8.4 LTS) at the latest patch level within the patch SLA.",
                "CRITICAL", [c("SELECT VERSION()"), " in the approved version list"], [c("SELECT VERSION()")], "PARTIAL"),
            ctl("MYSQL-AAA-001", "No anonymous or wildcard admin accounts", "AAA",
                "No anonymous accounts exist; root and admin accounts cannot log in from any host.",
                "CRITICAL", ["No row with ", c("user = ''"), "; root only on ", c("localhost"), "; no admin with ", c("host = '%'")],
                ["Query ", c("mysql.user")], "AUTOMATED"),
            ctl("MYSQL-AAA-002", "Password validation component", "AAA",
                "Password strength validation enforces the corporate password standard.",
                "HIGH", [c("validate_password.length"), " ≥ 14, ", c("validate_password.policy"), " = MEDIUM or STRONG, ",
                         c("password_history"), " ≥ 10, ", c("default_password_lifetime"), " ≤ 90"],
                [c("SHOW GLOBAL VARIABLES LIKE 'validate_password%'")], "AUTOMATED",
                "Service accounts may use PASSWORD EXPIRE NEVER when the password is rotated by PAM."),
            ctl("MYSQL-AAA-003", "Failed-login lockout", "AAA",
                "Accounts lock after repeated failed logins (8.0.19+), or connection-control throttling is enabled.",
                "MEDIUM", [c("FAILED_LOGIN_ATTEMPTS"), " ≤ 5 and ", c("PASSWORD_LOCK_TIME"), " ≥ 1 on human accounts"],
                ["Query ", c("mysql.user.User_attributes")], "PARTIAL"),
            ctl("MYSQL-PRIV-001", "Administrative privileges restricted", "PRIV",
                "FILE, SUPER, PROCESS, SHUTDOWN, CREATE USER, GRANT OPTION and dynamic admin privileges are held only by approved admin accounts.",
                "HIGH", ["Grantees match the approved admin list"],
                ["Query ", c("mysql.user"), " and ", c("mysql.global_grants")], "PARTIAL",
                "Tenable lists grantees; the reviewer compares with the approved list."),
            ctl("MYSQL-SVC-001", "Local file loading disabled", "SVC",
                "Clients cannot load local files into the server, and server-side file import / export is limited to one directory.",
                "HIGH", [c("local_infile = 0"), "; ", c("secure_file_priv"), " set to a dedicated directory or NULL"],
                [c("SHOW GLOBAL VARIABLES")], "AUTOMATED"),
            ctl("MYSQL-SVC-002", "Test database and sample data removed", "SVC",
                "The test database and any sample schemas are removed.",
                "LOW", [c("SHOW DATABASES"), " has no ", c("test"), " database"], [c("SHOW DATABASES")], "AUTOMATED"),
            ctl("MYSQL-SVC-003", "Strict SQL mode", "SVC",
                "The server rejects invalid data instead of silently truncating it.",
                "LOW", [c("sql_mode"), " includes ", c("STRICT_ALL_TABLES"), " or ", c("STRICT_TRANS_TABLES")],
                [c("SELECT @@GLOBAL.sql_mode")], "AUTOMATED"),
            ctl("MYSQL-CRYPTO-001", "Secure transport required", "CRYPTO",
                "All client and replication connections use TLS 1.2 or higher.",
                "HIGH", [c("require_secure_transport = ON"), "; ", c("tls_version = TLSv1.2,TLSv1.3")],
                [c("SHOW GLOBAL VARIABLES LIKE '%tls%'")], "AUTOMATED"),
            ctl("MYSQL-LOG-001", "Error and audit logging", "LOG",
                "The error log is written to a protected location and an audit log plugin / component records connections and privilege changes.",
                "HIGH", [c("log_error"), " set; audit log plugin active (Enterprise Audit, Percona or MariaDB audit plugin)"],
                [c("SHOW PLUGINS"), " / ", c("SHOW GLOBAL VARIABLES LIKE 'log_error%'")], "PARTIAL",
                "Community Edition has no bundled audit plugin; record the approved alternative."),
            ctl("MYSQL-OS-001", "Dedicated service account and file permissions", "OS",
                "mysqld runs as a dedicated non-root account; data directory and config files are readable only by that account.",
                "MEDIUM", [c("mysqld"), " runs as ", c("mysql"), "; ", c("datadir"), " mode 750 or stricter; ", c("my.cnf"), " not world-writable"],
                ["Unix audit: process owner and file permission checks"], "AUTOMATED"),
            ctl("MYSQL-OS-002", "No clear-text passwords on disk or in environment", "OS",
                "Passwords are not stored in my.cnf, scripts, shell history or the MYSQL_PWD variable. Use the login path or a vault.",
                "HIGH", ["No ", c("password="), " in option files; ", c("MYSQL_PWD"), " unset"],
                ["Unix audit: content check on option files"], "PARTIAL"),
        ],
        "example_query": "SELECT user, host FROM mysql.user\n WHERE user = '' OR (host = '%' AND user IN ('root', 'admin'));",
        "remediation": "DROP USER ''@'localhost';\nDROP USER ''@'%';\nRENAME USER 'root'@'%' TO 'root'@'localhost';",
    },
    {
        "slug": "04-mongodb",
        "short": "MongoDB",
        "product": "MongoDB Community / Enterprise Server (replica sets, sharded clusters)",
        "versions": "e.g., 7.0, 8.0",
        "prefix": "MONGO",
        "cis": "CIS MongoDB 7 / 8 Benchmark",
        "audit_file": "CIS_MongoDB_*.audit (database and mongod.conf checks via Unix audit)",
        "credential": "Database credential, type MongoDB, plus SSH credential for mongod.conf and file checks",
        "scan_account": ["Built-in ", c("clusterMonitor"), " and ", c("read"), " on ", c("admin"), "; no root or userAdmin roles"],
        "scope_notes": [
            ["Apply to every mongod and mongos, including arbiters and config servers."],
            ["MongoDB Atlas: controls Atlas enforces (TLS, authentication) are N/A; project-level settings are reviewed manually."],
            ["Audit logging and native encryption at rest need Enterprise; Community deployments use the compensating controls in Comments."],
        ],
        "controls": [
            ctl("MONGO-VER-001", "Supported release with patches", "VER",
                "The server runs a MongoDB release that is not past end of life, at the latest patch level within the patch SLA.",
                "CRITICAL", [c("db.version()"), " in the approved version list"], [c("buildInfo")], "PARTIAL"),
            ctl("MONGO-AAA-001", "Authorization enabled", "AAA",
                "Access control is on for every node. No node accepts unauthenticated connections.",
                "CRITICAL", [c("security.authorization: enabled")],
                ["Unix audit: ", c("mongod.conf"), "; database check: unauthenticated ", c("listDatabases"), " fails"], "AUTOMATED"),
            ctl("MONGO-AAA-002", "Strong authentication mechanism", "AAA",
                "Users authenticate with SCRAM-SHA-256, x.509, LDAP or Kerberos. SCRAM-SHA-1 is not allowed.",
                "HIGH", [c("setParameter.authenticationMechanisms"), " excludes ", c("SCRAM-SHA-1")],
                [c("getParameter: authenticationMechanisms")], "AUTOMATED"),
            ctl("MONGO-AAA-003", "Cluster member authentication", "AAA",
                "Replica set and shard members authenticate each other with x.509 certificates (keyFile only with an exception).",
                "HIGH", [c("security.clusterAuthMode: x509")], ["Unix audit: ", c("mongod.conf")], "AUTOMATED"),
            ctl("MONGO-PRIV-001", "Least-privilege roles", "PRIV",
                "root, userAdminAnyDatabase, dbOwner and clusterAdmin are granted only to approved administrators; applications use custom least-privilege roles.",
                "HIGH", ["Holders of the listed roles match the approved list"],
                [c("db.getSiblingDB('admin').system.users.find()"), " role listing"], "PARTIAL",
                "The reviewer compares role holders with the approved list."),
            ctl("MONGO-NET-001", "Bind to required interfaces only", "NET",
                "mongod listens only on localhost and the interfaces applications need.",
                "CRITICAL", [c("net.bindIp"), " does not contain ", c("0.0.0.0"), " or ", c("::"), "; ", c("net.bindIpAll"), " not true"],
                ["Unix audit: ", c("mongod.conf")], "AUTOMATED"),
            ctl("MONGO-CRYPTO-001", "TLS required", "CRYPTO",
                "All client and intra-cluster connections use TLS 1.2 or higher.",
                "HIGH", [c("net.tls.mode: requireTLS"), "; ", c("net.tls.disabledProtocols: TLS1_0,TLS1_1")],
                ["Unix audit: ", c("mongod.conf")], "AUTOMATED"),
            ctl("MONGO-CRYPTO-002", "Encryption at rest", "CRYPTO",
                "Databases classified Confidential or higher are encrypted at rest with keys held in KMIP / KMS.",
                "HIGH", [c("security.enableEncryption: true"), " with KMIP (Enterprise), or encrypted volumes (Community)"],
                ["Unix audit: ", c("mongod.conf")], "PARTIAL", "Volume encryption is checked by the OS / storage team."),
            ctl("MONGO-SVC-001", "Server-side JavaScript disabled", "SVC",
                "Server-side JavaScript ($where, mapReduce JS, $function) is disabled unless an application needs it.",
                "MEDIUM", [c("security.javascriptEnabled: false")], ["Unix audit: ", c("mongod.conf")], "AUTOMATED"),
            ctl("MONGO-LOG-001", "Audit and system logging", "LOG",
                "Authentication, authorization failures and user / role changes are audited and the logs are forwarded to the SIEM.",
                "HIGH", [c("auditLog.destination"), " set (Enterprise / Percona); ", c("systemLog.logAppend: true")],
                ["Unix audit: ", c("mongod.conf")], "PARTIAL",
                "Community: forward systemLog to the SIEM and record an exception for missing audit events."),
            ctl("MONGO-OS-001", "Dedicated service account and file permissions", "OS",
                "mongod runs as a dedicated non-root account; keyFile and certificate keys are mode 600; dbPath is owned by the service account.",
                "MEDIUM", ["Process owner ", c("mongod"), "; keyFile / PEM mode 600; dbPath mode 750 or stricter"],
                ["Unix audit: process owner and file permission checks"], "AUTOMATED"),
        ],
        "example_query": "db.adminCommand({ getCmdLineOpts: 1 }).parsed.security\ndb.adminCommand({ getParameter: 1, authenticationMechanisms: 1 })",
        "remediation": "# /etc/mongod.conf\nsecurity:\n  authorization: enabled\n  javascriptEnabled: false\nnet:\n  bindIp: 127.0.0.1,10.20.30.40\n  tls:\n    mode: requireTLS\n    disabledProtocols: TLS1_0,TLS1_1",
    },
    {
        "slug": "05-db2",
        "short": "IBM Db2",
        "product": "IBM Db2 for Linux, UNIX and Windows (LUW), including HADR",
        "versions": "e.g., 11.5.x",
        "prefix": "DB2",
        "cis": "CIS IBM Db2 11 Benchmark",
        "audit_file": "CIS_IBM_DB2_11_*.audit (database checks) + Unix audit for instance file permissions",
        "credential": "Database credential, type DB2 (database name and port; one entry per database)",
        "scan_account": [c("CONNECT"), " on each database, ", c("SELECT"), " on ", c("SYSCAT"), " views, SYSMON authority; no SYSADM / DBADM"],
        "scope_notes": [
            ["Instance (DBM CFG) controls apply once per instance; database (DB CFG) controls apply to every database in the instance."],
            ["Db2 for z/OS and Db2 for i are out of scope of this page."],
        ],
        "controls": [
            ctl("DB2-VER-001", "Supported release with current fix pack", "VER",
                "The instance runs a supported Db2 release at the latest mod pack / fix pack within the patch SLA.",
                "CRITICAL", [c("db2level"), " in the approved version list"], [c("SELECT * FROM SYSIBMADM.ENV_INST_INFO")], "PARTIAL"),
            ctl("DB2-AAA-001", "Server-side authentication", "AAA",
                "The instance authenticates users on the server with encrypted credentials and does not trust client authentication.",
                "CRITICAL", [c("AUTHENTICATION = SERVER_ENCRYPT"), " (or KERBEROS / GSSPLUGIN); ",
                             c("TRUST_ALLCLNTS = NO"), "; ", c("TRUST_CLNTAUTH = SERVER")],
                ["Query ", c("SYSIBMADM.DBMCFG")], "AUTOMATED"),
            ctl("DB2-AAA-002", "Dedicated authority groups", "AAA",
                "SYSADM, SYSCTRL, SYSMAINT and SYSMON authorities map to dedicated OS groups with approved members.",
                "HIGH", [c("SYSADM_GROUP"), ", ", c("SYSCTRL_GROUP"), ", ", c("SYSMAINT_GROUP"), ", ", c("SYSMON_GROUP"), " set to dedicated groups"],
                ["Query ", c("SYSIBMADM.DBMCFG"), "; group membership via Unix audit"], "PARTIAL"),
            ctl("DB2-PRIV-001", "PUBLIC privileges revoked", "PRIV",
                "PUBLIC holds no database authorities; databases are created RESTRICTIVE or the defaults are revoked.",
                "HIGH", ["No ", c("CONNECTAUTH"), ", ", c("CREATETABAUTH"), ", ", c("BINDADDAUTH"), ", ", c("IMPLSCHEMAAUTH"),
                         " for PUBLIC in ", c("SYSCAT.DBAUTH")],
                ["Query ", c("SYSCAT.DBAUTH WHERE GRANTEE = 'PUBLIC'")], "AUTOMATED"),
            ctl("DB2-PRIV-002", "Separation of duties for SECADM", "PRIV",
                "SECADM is held by a security administrator who does not hold DBADM or DATAACCESS.",
                "HIGH", ["No grantee holds SECADM together with DBADM or DATAACCESS"],
                ["Query ", c("SYSCAT.DBAUTH")], "AUTOMATED"),
            ctl("DB2-PRIV-003", "Catalog access restricted", "PRIV",
                "SELECT on the system catalog is not granted to PUBLIC where applications do not need it.",
                "MEDIUM", ["No PUBLIC SELECT on ", c("SYSCAT.*"), " / ", c("SYSIBM.*"), " (RESTRICT_ACCESS = YES)"],
                ["Query ", c("SYSCAT.TABAUTH")], "AUTOMATED"),
            ctl("DB2-CRYPTO-001", "TLS-only communication", "CRYPTO",
                "Clients connect over TLS 1.2 or higher; plaintext TCP/IP is disabled.",
                "HIGH", [c("DB2COMM = SSL"), "; ", c("SSL_VERSIONS = TLSV12,TLSV13"), "; ", c("SSL_SVR_KEYDB"), " set"],
                ["Query ", c("SYSIBMADM.DBMCFG"), "; ", c("db2set -all")], "AUTOMATED"),
            ctl("DB2-CRYPTO-002", "Native encryption at rest", "CRYPTO",
                "Databases classified Confidential or higher use Db2 native encryption with a keystore (PKCS#12 or KMIP).",
                "HIGH", [c("ENCRYPTED = YES"), " in ", c("SYSPROC.ADMIN_GET_ENCRYPTION_INFO")],
                [c("SELECT * FROM TABLE(SYSPROC.ADMIN_GET_ENCRYPTION_INFO())")], "PARTIAL",
                "Data classification comes from the CMDB."),
            ctl("DB2-LOG-001", "db2audit configured", "LOG",
                "The instance audit facility records security-relevant categories and is archived to the SIEM.",
                "HIGH", [c("AUDIT"), ", ", c("CHECKING"), ", ", c("OBJMAINT"), ", ", c("SECMAINT"), ", ", c("SYSADMIN"), ", ",
                         c("VALIDATE"), " = BOTH; database audit policy assigned"],
                [c("db2audit describe"), " via Unix audit; ", c("SYSCAT.AUDITPOLICIES")], "PARTIAL"),
            ctl("DB2-NET-001", "Discovery disabled", "NET",
                "The instance and databases cannot be discovered by DB2 discovery requests.",
                "MEDIUM", [c("DISCOVER = DISABLE"), "; ", c("DISCOVER_INST = DISABLE"), "; ", c("DISCOVER_DB = DISABLE")],
                ["Query ", c("SYSIBMADM.DBMCFG"), " / ", c("SYSIBMADM.DBCFG")], "AUTOMATED"),
            ctl("DB2-OS-001", "Instance owner and file permissions", "OS",
                "The instance runs under a dedicated non-root owner; the instance home and sqllib directories are not writable by others.",
                "MEDIUM", ["Instance owner ≠ root; ", c("sqllib"), " and database paths mode 750 or stricter"],
                ["Unix audit: file permission checks"], "AUTOMATED"),
        ],
        "example_query": "SELECT NAME, VALUE FROM SYSIBMADM.DBMCFG\n WHERE NAME IN ('authentication', 'trust_allclnts', 'trust_clntauth', 'discover');",
        "remediation": "db2 update dbm cfg using AUTHENTICATION SERVER_ENCRYPT TRUST_ALLCLNTS NO TRUST_CLNTAUTH SERVER\ndb2stop\ndb2start",
    },
    {
        "slug": "06-teradata",
        "short": "Teradata",
        "product": "Teradata Vantage (on-premises / VantageCore, VantageCloud Enterprise)",
        "versions": "e.g., 17.20, 20.00",
        "prefix": "TD",
        "cis": "No CIS Benchmark is published. Company baseline derived from the Teradata Vantage Security Administration guide and DB-COM controls",
        "audit_file": "No Tenable database audit for Teradata. Planned: custom Unix audit running BTEQ queries on a TPA node (cmd_exec)",
        "credential": "SSH credential to a TPA node for the custom audit; until then MANUAL review",
        "scan_account": [c("SELECT"), " on the ", c("DBC"), " dictionary views listed below; no DBC or security administrator rights"],
        "scope_notes": [
            [("b", "No CIS Benchmark and no native Tenable database checks. "),
             "Every control on this page is reviewed MANUALLY until the custom audit is built (see the Automation status in each row)."],
            ["Node OS (SLES) hardening follows the company Linux standard and is scanned by the Tenable Unix audit."],
            ["VantageCloud Lake: controls the provider manages are N/A."],
        ],
        "controls": [
            ctl("TD-VER-001", "Supported release with current PUT / patches", "VER",
                "The system runs a supported Vantage release and current efixes within the patch SLA.",
                "CRITICAL", [c("SELECT InfoData FROM DBC.DBCInfoV"), " in the approved version list"],
                ["Manual: query ", c("DBC.DBCInfoV")], "MANUAL"),
            ctl("TD-AAA-001", "DBC user protected", "AAA",
                "The DBC user is not used for daily administration, has a vaulted password, and can log on only from approved hosts.",
                "CRITICAL", ["DBC password in PAM; logon rules limit DBC to approved hosts; no direct DBC sessions in ", c("DBC.LogOnOffV"), " outside break-glass"],
                ["Manual: ", c("DBC.LogonRulesV"), " and ", c("DBC.LogOnOffV")], "MANUAL"),
            ctl("TD-AAA-002", "System password and lockout defaults", "AAA",
                "System-wide password defaults meet the corporate password standard.",
                "HIGH", [c("PasswordMinChar"), " ≥ 14, digits and special characters required, ", c("MaxLogonAttempts"), " ≤ 5, ",
                         c("LockedUserExpire"), " ≥ 30 min, ", c("ExpirePassword"), " ≤ 90 days, ", c("PasswordReuse"), " ≥ 365 days"],
                ["Manual: ", c("SELECT * FROM DBC.SysSecDefaults")], "PLANNED"),
            ctl("TD-AAA-003", "Central authentication", "AAA",
                "Human users authenticate through LDAP / Kerberos (TDGSS). TD2 (database) authentication is limited to service and break-glass accounts.",
                "HIGH", ["Default mechanism LDAP or KRB5 in TDGSS config; TD2 users listed and approved"],
                ["Manual: TDGSS configuration on the TPA node"], "MANUAL"),
            ctl("TD-PRIV-001", "Role-based access, no PUBLIC grants", "PRIV",
                "Access is granted through roles. Nothing is granted to PUBLIC or ALL beyond defaults, and WITH GRANT OPTION is limited to administrators.",
                "HIGH", ["No user-level grants outside admin accounts in ", c("DBC.AllRightsV"), "; no ", c("GrantAuthority = 'Y'"), " to non-admins"],
                ["Manual: ", c("DBC.AllRightsV"), ", ", c("DBC.AllRoleRightsV")], "PLANNED"),
            ctl("TD-PRIV-002", "Dictionary access restricted", "PRIV",
                "Users see only the dictionary rows about objects they can access (X views), and direct access to DBC tables is revoked from PUBLIC.",
                "MEDIUM", ["Applications use ", c("DBC.*VX"), " views; PUBLIC SELECT on DBC tables revoked"],
                ["Manual: ", c("DBC.AllRightsV WHERE UserName = 'PUBLIC'")], "MANUAL"),
            ctl("TD-CRYPTO-001", "Encryption in transit", "CRYPTO",
                "Client connections are encrypted with TLS (Vantage 17.10+) or TDGSS confidentiality.",
                "HIGH", ["TLS enabled on the gateway with TLS 1.2+, or TDGSS ", c("ConfidentialityRequired"), " = yes (AES-256)"],
                ["Manual: gateway (", c("gtwcontrol"), ") and TDGSS configuration"], "MANUAL"),
            ctl("TD-CRYPTO-002", "Encryption at rest", "CRYPTO",
                "Systems holding Confidential data use self-encrypting drives or Vantage storage encryption; backups are encrypted.",
                "HIGH", ["SED / storage encryption enabled; backup encryption enabled in DSA / BAR"],
                ["Manual: platform evidence from Teradata support"], "NOT FEASIBLE",
                "Not visible from SQL; evidence collected annually."),
            ctl("TD-LOG-001", "Access logging and DBQL", "LOG",
                "Logons, failed logons, grants / revokes and access to sensitive objects are logged; DBQL is enabled; logs are forwarded to the SIEM.",
                "HIGH", ["Access logging rules in ", c("DBC.AccLogRulesV"), " for GRANT, REVOKE, CREATE / DROP USER; DBQL active in ", c("DBC.DBQLRulesV")],
                ["Manual: ", c("DBC.AccLogRulesV"), ", ", c("DBC.DBQLRulesV")], "PLANNED"),
            ctl("TD-NET-001", "Logon rules restrict client hosts", "NET",
                "Logon rules allow each privileged user only from approved client hosts.",
                "MEDIUM", [c("GRANT LOGON ON <host> TO <user>"), " rules present for privileged users"],
                ["Manual: ", c("DBC.LogonRulesV")], "MANUAL"),
        ],
        "example_query": "SELECT PasswordMinChar, PasswordDigits, PasswordSpecChar,\n       MaxLogonAttempts, LockedUserExpire, ExpirePassword, PasswordReuse\n  FROM DBC.SysSecDefaults;",
        "remediation": "UPDATE DBC.SysSecDefaults\n   SET PasswordMinChar = 14, MaxLogonAttempts = 5, ExpirePassword = 90, PasswordReuse = 365;\n-- takes effect after the next system restart or tpareset; follow the change process",
    },
]


# ---------------------------------------------------------------- shared bits

def changelog_table():
    return (
        "table",
        ["Version", "Date", "Author", "Change", "Approved by"],
        [
            ["0.1", "YYYY-MM-DD", ph("Name"), "Initial draft", ph("Name")],
            [ph("x.y"), "YYYY-MM-DD", ph("Name"), ph("What changed"), ph("Name")],
        ],
    )


def policy_banner():
    return ("panel", "warning", f"Company policy – {POLICY_ID}", [
        ("p", [f"This page is part of the company {POLICY_TITLE} ({POLICY_ID}). "
               "Its requirements are mandatory for every database in scope. "
               "Deviations need an approved entry in the DB Security – Exceptions Register. "
               "CIS Benchmarks and Tenable audit files are the technical basis and assessment method; "
               "where this policy differs from CIS, this policy applies."]),
    ])


def legends():
    return [
        ("h", 3, "Severity and remediation timelines"),
        (
            "table",
            ["Severity", "Meaning", "Remediate within (production)", "Remediate within (non-production)"],
            [
                [[sev("CRITICAL")], "Direct path to unauthorized access or data exposure", "15 days", "30 days"],
                [[sev("HIGH")], "Significant weakness in authentication, privileges, encryption or auditing", "30 days", "60 days"],
                [[sev("MEDIUM")], "Hardening gap with limited direct exposure", "90 days", "120 days"],
                [[sev("LOW")], "Best practice or hygiene item", "Next maintenance window", "Next maintenance window"],
            ],
        ),
        ("p", [("i", "Timelines run from the Tenable scan date that first reports the failure. Align them with the corporate vulnerability management standard before approval.")]),
        ("h", 3, "Assessment status"),
        (
            "table",
            ["Status", "Meaning"],
            [
                [[asm("AUTOMATED")], "The Tenable audit fully assesses the requirement; PASS / FAIL comes from the scan"],
                [[asm("PARTIAL")], "Tenable collects the data but a reviewer completes the check (e.g., against an approved list)"],
                [[asm("MANUAL")], "A DBA or reviewer collects evidence by hand during the review"],
                [[asm("PLANNED")], "A custom audit check is being built"],
                [[asm("NOT FEASIBLE")], "Cannot be assessed from the database or host; evidence is collected another way"],
            ],
        ),
    ]


# ---------------------------------------------------------------- pages

def overview_page():
    platform_rows = [
        [p["short"], p["product"], ph(p["versions"]), p["cis"], [("code", p["prefix"])], f"DB Security – {p['short']}"]
        for p in PLATFORMS
    ]
    coverage_table = (
        "table",
        ["Platform", "Controls", "Automated", "Partial", "Manual / planned", "Compliance % (last scan)", "Open CRITICAL / HIGH", "Last scan"],
        [[p["short"], str(len(p["controls"])),
          str(sum(1 for x in p["controls"] if x["status"] == "AUTOMATED")),
          str(sum(1 for x in p["controls"] if x["status"] == "PARTIAL")),
          str(sum(1 for x in p["controls"] if x["status"] in ("MANUAL", "PLANNED", "NOT FEASIBLE"))),
          "0%", "0", "YYYY-MM-DD"] for p in PLATFORMS],
    )
    matrix = []
    for cid, _, req, _ in COMMON_BASELINE:
        row = [[("b", cid)], req]
        for p in PLATFORMS:
            ids = [x["id"] for x in p["controls"] if x["id"] in BASELINE_MAP[cid]]
            row.append(", ".join(ids) if ids else ph("Gap – add control or N/A"))
        matrix.append(row)
    return [
        ("props", "dbsec-policy", [
            ("Policy ID", [("code", POLICY_ID)]),
            ("Policy type", "Company policy – technical security standard"),
            ("Policy owner", ph("CISO / Head of Information Security")),
            ("Maintained by", ph("Database Engineering & Security Architecture")),
            ("Approver", ph("Name, role")),
            ("Version", "0.1"),
            ("Policy status", [("st", "Grey", "DRAFT")]),
            ("Effective date", "YYYY-MM-DD"),
            ("Next review due", "YYYY-MM-DD (12 months after approval)"),
            ("Classification", "Internal"),
        ]),
        policy_banner(),
        ("toc", 2),
        ("h", 2, "1. Purpose"),
        ("p", ["This policy sets the minimum security configuration for every company database. "
               "It protects the confidentiality, integrity and availability of company and customer data, "
               "and gives auditors one place to see each requirement, how Tenable assesses it, and the current compliance status."]),
        ("h", 2, "2. Policy statement"),
        ("ul", [
            ["Every database in scope ", ("b", "must"), " be configured to meet the controls on its platform page before it goes into production, and must stay compliant for its whole life."],
            ["Database configuration compliance ", ("b", "must"), " be assessed with Tenable using the approved audit files on the schedule in section 6."],
            ["Failed controls ", ("b", "must"), " be remediated within the timelines in section 7, or covered by an approved, time-limited exception."],
            ["New database platforms or major versions ", ("b", "must not"), " go into production until a platform page for them is approved."],
        ]),
        ("h", 2, "3. Scope"),
        ("p", ["All database instances owned or operated by the company, or operated for it by a third party, in production, DR, UAT and development environments, on-premises or in the cloud (IaaS). "
               "Managed database services (PaaS) are in scope for the controls the company can configure."]),
        ("table", ["Platform", "Product", "Versions in scope", "Technical basis", "Control prefix", "Platform page"], platform_rows),
        ("p", [("b", "Out of scope: "), ("ph", "e.g., embedded databases inside vendor appliances, developer workstations, decommissioned systems")]),
        ("h", 2, "4. Roles and responsibilities"),
        ("table", ["Role", "Responsibilities"], [
            [[("b", "Policy owner (CISO)")], "Approves the policy and exceptions rated CRITICAL; reports compliance to the risk committee"],
            [[("b", "Database Engineering / DBAs")], "Build databases to this policy, remediate findings, keep platform pages and control values current"],
            [[("b", "Vulnerability Management (Tenable)")], "Maintain scan policies, audit files and credentials; run scans; publish compliance results"],
            [[("b", "Application / data owners")], "Approve access, classify data, accept risk for exceptions on their systems"],
            [[("b", "Security Operations (SOC)")], "Receive and monitor database audit logs in the SIEM"],
            [[("b", "Internal Audit")], "Independently test compliance with this policy"],
        ]),
        ("h", 2, "5. Common baseline (all platforms)"),
        ("p", ["Every platform page implements these company-wide requirements. Platform pages may be stricter, never weaker."]),
        ("table", ["ID", "Domain", "Requirement", "Minimum value"],
         [[[("b", r[0])], [("code", r[1])], r[2], r[3]] for r in COMMON_BASELINE]),
        ("h", 2, "6. Compliance assessment with Tenable"),
        ("table", ["Item", "Requirement"], [
            [[("b", "Scan template")], ["Tenable ", ("b", "Policy Compliance Auditing"), " (credentialed), with the audit files listed on each platform page"]],
            [[("b", "Audit files")], "CIS-based Tenable audit files, tailored to the company values on the platform pages. Tailored copies are version-controlled and the version is recorded on each platform page"],
            [[("b", "Credentials")], "Dedicated read-only scan account per platform (privileges on each platform page), stored in Tenable / PAM, never a DBA account"],
            [[("b", "Frequency")], "Production: monthly and after every major change or upgrade. Non-production: quarterly. New builds: before go-live"],
            [[("b", "Targets")], "Asset lists synchronized from the CMDB database inventory; every instance in scope is scanned"],
            [[("b", "Compliance target")], "100% of CRITICAL and HIGH controls passing (or covered by an exception); ≥ 95% of all controls"],
            [[("b", "Results")], "Published to the compliance dashboard below; failed controls raise remediation tickets for the owning team"],
            [[("b", "Manual controls")], "Controls marked MANUAL / PARTIAL are reviewed quarterly; evidence is attached to the review ticket"],
        ]),
        ("h", 2, "7. Severity, remediation and status legend"),
        *legends(),
        ("h", 2, "8. Compliance dashboard"),
        ("alt", [
            ("p", ["The report below reads the Page Properties table on each platform page. Platform pages need the label ",
                   ("code", "dbsec-platform"), " to appear here."]),
            ("report", 'label = "dbsec-platform" and space = currentSpace()',
             "Platform,Controls,Automated (Tenable),Compliance % (last scan),Open CRITICAL / HIGH,Last Tenable scan,Owner team"),
            ("expand", "Manual compliance table (use if the report macro is not available)", [coverage_table]),
        ], [
            ("p", ["Copy these numbers from the summary table at the top of each platform page after every scan."]),
            coverage_table,
        ]),
        ("h", 2, "9. Cross-platform control matrix"),
        ("p", ["Platform controls that implement each common baseline requirement. A gap means the requirement is assessed by another process "
               "(e.g., backups by the backup standard, host hardening by the OS standard) or a control still has to be written."]),
        ("table", ["Baseline", "Requirement"] + [p["short"] for p in PLATFORMS], matrix),
        ("h", 2, "10. Exceptions"),
        ("ul", [
            ["Any control that cannot be met needs an exception in ", ("b", "DB Security – Exceptions Register"), " before the remediation deadline."],
            ["Exceptions have a named risk owner, a compensating control and an expiry date of at most 12 months."],
            ["CRITICAL exceptions are approved by the policy owner; others by the Head of Database Engineering and the application owner."],
            ["Approved exceptions are applied as exclusions in Tenable so they are not reported as failures, and are re-reviewed at expiry."],
        ]),
        ("h", 2, "11. Non-compliance"),
        ("p", ["Overdue findings without an approved exception are escalated to the system owner's management and reported to the risk committee. "
               "Databases with open CRITICAL findings may be isolated from the network. "
               "Wilful breach of this policy may lead to disciplinary action under the company code of conduct."]),
        ("h", 2, "12. Control ID convention"),
        ("p", ["Format: ", ("code", "<PREFIX>-<DOMAIN>-<NNN>"), ", for example ", ("code", "ORA-AAA-001"), ". Prefixes: ",
               ", ".join(f"{p['prefix']} {p['short']}" for p in PLATFORMS),
               ". Control IDs are never renumbered or reused; retired controls are struck through with ", ("code", "RETIRED vX.Y"), " in Comments."]),
        ("table", ["Domain code", "Domain", "Typical controls"],
         [[[("code", d)], n, t] for d, n, t in DOMAINS]),
        ("h", 2, "13. Policy review"),
        ("ul", [
            ["This policy is reviewed at least ", ("b", "annually"), " and approved by the policy owner."],
            ["Platform pages are also reviewed after a new CIS Benchmark or Tenable audit file release, a major database version, or an audit finding."],
            ["When a new benchmark version is adopted, record the benchmark and audit file versions on the platform page and update the CIS Reference column."],
        ]),
        ("h", 2, "14. Change log"),
        changelog_table(),
        ("h", 2, "15. References"),
        ("ul", [
            ["CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks (basis for control values; licence terms apply to benchmark content)"],
            ["Tenable compliance audit files: https://www.tenable.com/audits"],
            ["Corporate Information Security Policy: ", ("ph", "add link")],
            ["Corporate password standard: ", ("ph", "add link")],
            ["Vulnerability management standard (remediation SLAs): ", ("ph", "add link")],
            ["Data classification standard: ", ("ph", "add link")],
        ]),
    ]


def control_row(x):
    return [
        [("b", x["id"])], x["name"], [("code", x["dom"])], x["req"], [sev(x["sev"])],
        x["val"], x["check"], ph("CIS § from .audit"), [asm(x["status"])],
        ph("YYYY-MM-DD / Name"), x["comment"] or " ",
    ]


def platform_page(p):
    pre = p["prefix"]
    ctls = p["controls"]
    n_auto = sum(1 for x in ctls if x["status"] == "AUTOMATED")
    blank = [
        ph(f"{pre}-DOMAIN-NNN"), ph("Short control name"), ph("Domain"),
        ph("What must be true"), ph("CRITICAL / HIGH / MEDIUM / LOW"),
        ph("Value that passes"), ph("Audit item / query + pass condition"), ph("CIS §"),
        ph("AUTOMATED / PARTIAL / MANUAL / PLANNED / NOT FEASIBLE"),
        ph("YYYY-MM-DD / Name"), ph("Caveats, exception IDs"),
    ]
    detail_fields = [
        ("Applies to", ph("All instances / production only / CDB only / ...")),
        ("Rationale / risk", ph("Why the control exists; what happens if it is not met")),
        ("Tenable audit item", ph("Description string of the check in the .audit file")),
        ("Audit file and version", ph("File name, version, date")),
        ("Check type", ph("SQL query / config file / registry / manual")),
        ("Pass condition", ph("Exact condition")),
        ("Not applicable when", ph("e.g., feature not installed or not licensed")),
        ("Remediation impact", ph("None / restart required / application change")),
        ("CIS reference", ph("Benchmark name, version, section")),
        ("Exceptions", ph("EXC-IDs, or None")),
    ]
    return [
        ("props", "dbsec-platform", [
            ("Platform", p["short"]),
            ("Product", p["product"]),
            ("Versions in scope", ph(p["versions"])),
            ("Policy", [("code", POLICY_ID)]),
            ("Technical basis", p["cis"]),
            ("Tenable audit file(s)", p["audit_file"]),
            ("Tenable credential", p["credential"]),
            ("Control prefix", [("code", pre)]),
            ("Instances in scope", ph("count or link to CMDB")),
            ("Controls", str(len(ctls))),
            ("Automated (Tenable)", f"{n_auto} of {len(ctls)}"),
            ("Compliance % (last scan)", "0%"),
            ("Open CRITICAL / HIGH", "0"),
            ("Last Tenable scan", "YYYY-MM-DD"),
            ("Owner team", ph("Team")),
            ("Next review due", "YYYY-MM-DD"),
        ]),
        policy_banner(),
        ("toc", 2),
        ("h", 2, "Scope & applicability"),
        ("ul", p["scope_notes"]),
        ("h", 2, "Tenable assessment setup"),
        ("table", ["Item", "Value"], [
            [[("b", "Scan template")], "Policy Compliance Auditing (credentialed)"],
            [[("b", "Audit file(s)")], p["audit_file"]],
            [[("b", "Credential")], p["credential"]],
            [[("b", "Scan account privileges")], p["scan_account"]],
            [[("b", "Tailoring")], ["Company values from the register below override CIS defaults in the tailored audit file. Store it in ",
                                    ("ph", "repository / Tenable policy name")]],
        ]),
        ("h", 2, "Control register"),
        ("panel", "info", "How to maintain this register", [
            ("ul", [
                ["One row per control. Control IDs are never renumbered or reused."],
                [("b", "Tenable Check"), " describes what the audit item reads and its pass condition. Copy the CIS section from the audit item's ",
                 ("code", "reference"), " field into ", ("b", "CIS Reference"), "."],
                ["Changing a Compliant Value is a policy change: record it in the change log and get approval."],
                ["After every scan, update Compliance % and Open CRITICAL / HIGH in the table at the top of the page."],
            ]),
        ]),
        ("table", CONTROL_COLUMNS, [control_row(x) for x in ctls] + [blank]),
        ("h", 2, "Control details"),
        ("p", ["Optional. Copy this expand for each control that needs more detail than the register holds."]),
        ("expand", f"{ctls[0]['id']} – {ctls[0]['name']} – details (example)", [
            ("table", ["Field", "Value"], [[[("b", k)], v] for k, v in detail_fields]),
            ("p", [("b", "Evidence query (example, verify before use):")]),
            ("code", p["example_query"]),
            ("p", [("b", "Remediation (example, apply through change management):")]),
            ("code", p["remediation"]),
            ("p", [("b", "Review history")]),
            ("table", ["Date", "Reviewed by", "Outcome", "Notes"],
             [["YYYY-MM-DD", ph("Name"), ph("Compliant / remediated / exception raised"), ph("Notes")]]),
        ]),
        ("h", 2, "Known Tenable limitations & false positives"),
        ("table", ["Control ID", "Limitation / false-positive scenario", "Impact", "Workaround"],
         [[ph(f"{pre}-DOMAIN-NNN"), ph("What the audit gets wrong"), ph("Missed FAIL / false FAIL"), ph("Manual step or audit tailoring")]]),
        ("h", 2, "Page change log"),
        changelog_table(),
    ]


def exceptions_page():
    return [
        policy_banner(),
        ("panel", "note", "Before you add an exception", [
            ("ul", [
                ["Every exception needs a business justification, a compensating control, a named risk owner and an expiry date (max. 12 months)."],
                ["CRITICAL controls: approval by the policy owner (CISO). Others: Head of Database Engineering and the application owner."],
                ["Ask Vulnerability Management to exclude the instance from that Tenable audit item, and record it in ", ("b", "Excluded in Tenable?"), "."],
                ["Put the Exception ID in the Comments column of the control on its platform page."],
            ]),
        ]),
        ("h", 2, "Status"),
        ("table", ["Status", "Meaning"], [
            [[("st", "Green", "ACTIVE")], "Approved and within its expiry date"],
            [[("st", "Yellow", "EXPIRING")], "Expires within 30 days; renew or remediate"],
            [[("st", "Red", "EXPIRED")], "Past expiry; the instance is non-compliant"],
            [[("st", "Grey", "CLOSED")], "Remediated or no longer needed"],
        ]),
        ("h", 2, "Register"),
        ("table",
         ["Exception ID", "Control ID", "Platform", "Instances / databases", "Business justification",
          "Compensating control", "Risk owner", "Approved by / on", "Expires on", "Excluded in Tenable?", "Status"],
         [[[("b", "DBEXC-001")], ph("MSSQL-SVC-002"), ph("Microsoft SQL Server"), ph("Instance names / CMDB IDs"),
           ph("e.g., Database Mail needed for application alerts"), ph("e.g., SMTP relay restricted to internal domain"),
           ph("Name, role"), ph("Name / YYYY-MM-DD"), "YYYY-MM-DD", ph("Yes / No"), [("st", "Green", "ACTIVE")]]]),
    ]


def all_pages():
    parent = POLICY_TITLE
    pages = [{
        "slug": "00-policy",
        "title": parent,
        "tab": "Policy",
        "cat": "Parent page",
        "parent": None,
        "label": "dbsec, company-policy",
        "blocks": overview_page(),
    }]
    for p in PLATFORMS:
        pages.append({
            "slug": p["slug"],
            "title": f"DB Security – {p['short']}",
            "tab": p["short"],
            "cat": "Platform standard",
            "parent": parent,
            "label": "dbsec, dbsec-platform, company-policy",
            "blocks": platform_page(p),
        })
    pages.append({
        "slug": "07-exceptions",
        "title": "DB Security – Exceptions Register",
        "tab": "Exceptions",
        "cat": "Register",
        "parent": parent,
        "label": "dbsec, dbsec-exceptions",
        "blocks": exceptions_page(),
    })
    return pages
