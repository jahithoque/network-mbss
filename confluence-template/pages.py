"""Content model for the Network MBSS Confluence pages.

Every page is a list of blocks. build.py renders the same blocks to
Confluence storage format, Confluence wiki markup and HTML, so the three
outputs never drift apart. Edit content here, then run `python3 build.py`.

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

Inlines are a string or a list of: str, ("b", s), ("i", s), ("code", s),
("st", colour, title) status lozenge, ("ph", s) placeholder, ("br",).
"""

# ---------------------------------------------------------------- legends

SEVERITY = {
    "CRITICAL": "Red",
    "HIGH": "Yellow",
    "MEDIUM": "Blue",
    "LOW": "Grey",
}

AUTOMATION = {
    "AUTOMATED": "Green",
    "PARTIAL": "Yellow",
    "MANUAL": "Blue",
    "PLANNED": "Purple",
    "NOT FEASIBLE": "Grey",
}


def sev(name):
    return ("st", SEVERITY[name], name)


def auto(name):
    return ("st", AUTOMATION[name], name)


def ph(text):
    return [("ph", text)]


RULE_COLUMNS = [
    "Rule ID",
    "Rule Name",
    "Domain",
    "Description / Requirement",
    "Severity",
    "Expected (Compliant) Value",
    "Current Check (Automation Tool)",
    "Old Check",
    "Automation Status",
    "Last Review (Date / By)",
    "Comments",
]

DOMAINS = [
    ("MGMT", "Management plane access", "SSH/HTTPS only, management ACLs or allow-lists, session timeouts"),
    ("AAA", "Authentication & authorization", "TACACS+/RADIUS, local fallback account, password policy, RBAC"),
    ("CRYPTO", "Cryptography", "TLS versions, cipher suites, key lengths, certificate validity"),
    ("LOG", "Logging & monitoring", "Remote syslog, log levels, timestamps, audit logging"),
    ("NTP", "Time synchronization", "Approved NTP servers, NTP authentication"),
    ("SNMP", "SNMP", "SNMPv3 only, no default communities, ACL-restricted"),
    ("SVC", "Service hardening", "Unused services disabled (HTTP server, CDP, Telnet, small servers)"),
    ("BANNER", "Legal banners", "Login / MOTD warning banner"),
    ("POL", "Policy / rulebase", "No any-any rules, cleanup rule, logging on rules, default deny"),
    ("CTRL", "Control plane", "Control-plane policing, routing protocol authentication"),
    ("HA", "Availability & backup", "HA sync, configuration backup"),
    ("VER", "Software & patching", "Approved OS version, end-of-life / end-of-support"),
]

# ---------------------------------------------------------------- platforms

PLATFORMS = [
    {
        "slug": "01-checkpoint",
        "title": "MBSS – Firewall – Check Point",
        "short": "Check Point",
        "category": "Firewall",
        "product": "Check Point Security Gateways & Security Management (Gaia OS)",
        "versions": "e.g., R81.20, R82",
        "prefix": "CP",
        "components": "Gaia OS (gateways), Gaia OS (management server), security policy / rulebase, log server",
        "sources": [
            [("code", "clish"), ": ", ("code", "show configuration"), ", ", ("code", "show password-controls all")],
            ["Management API: ", ("code", "mgmt_cli show access-rulebase"), " (JSON)"],
            ["Expert mode files where no clish/API equivalent exists"],
        ],
        "scope_notes": [
            [("b", "CP-POL rules"), " apply to the security policy on the management server, not to individual gateways."],
            ["State in ", ("b", "Comments"), " when a rule applies only to gateways or only to management servers."],
            ["Note inline layers and shared layers when the rulebase check does not parse them."],
        ],
        "example": [
            "CP-AAA-001",
            "Gaia password minimum length",
            "AAA",
            "Local Gaia accounts must use a minimum password length of 14 characters.",
            [sev("HIGH")],
            [("code", "min-password-length"), " is 14 or higher"],
            ["clish ", ("code", "show password-controls all"), "; parse minimum password length; PASS if ≥ 14"],
            ["Manual check in Gaia WebUI › User Management › Password Policy"],
            [auto("AUTOMATED")],
            "2026-09-30 / Reviewer name",
            "Applies to gateways and management servers. Moved from manual to automated check in v1.1.",
        ],
        "remediation": "set password-controls min-password-length 14\nsave config",
    },
    {
        "slug": "02-bluecoat",
        "title": "MBSS – Proxy – BlueCoat ProxySG",
        "short": "BlueCoat",
        "category": "Proxy",
        "product": "Symantec BlueCoat ProxySG / Edge SWG (SGOS)",
        "versions": "e.g., SGOS 7.3.x",
        "prefix": "BC",
        "components": "SGOS system settings, management services, proxy policy (VPM / CPL), authentication realms",
        "sources": [
            ["SGOS CLI: ", ("code", "show config")],
            ["Policy export (VPM / CPL) for policy rules"],
            ["Management Console where no CLI equivalent exists"],
        ],
        "scope_notes": [
            [("b", "BC-POL rules"), " are checked against the installed policy, not the VPM draft."],
            ["State in ", ("b", "Comments"), " when a rule applies only to explicit or only to transparent deployments."],
        ],
        "example": [
            "BC-MGMT-001",
            "Disable Telnet and HTTP management consoles",
            "MGMT",
            "Only encrypted management services (HTTPS-Console, SSH-Console) may be enabled.",
            [sev("HIGH")],
            ["Telnet-Console and HTTP-Console disabled; HTTPS-Console and SSH-Console enabled"],
            [("code", "show config"), " › management-services section; FAIL if Telnet-Console or HTTP-Console is enabled"],
            ["Regex matched Telnet-Console only; HTTP-Console was not checked"],
            [auto("AUTOMATED")],
            "2026-09-30 / Reviewer name",
            "Old check missed HTTP-Console. Updated in v1.1.",
        ],
        "remediation": "#(config) management-services\n#(config management-services) disable Telnet-Console\n#(config management-services) disable HTTP-Console",
    },
    {
        "slug": "03-f5",
        "title": "MBSS – Load Balancer – F5 BIG-IP",
        "short": "F5 BIG-IP",
        "category": "Load Balancer",
        "product": "F5 BIG-IP (LTM / GTM / ASM / APM) on TMOS",
        "versions": "e.g., 15.1.x, 17.1.x",
        "prefix": "F5",
        "components": "TMOS system & management, management port and self IPs, LTM objects (virtual servers, profiles, SSL), provisioned modules",
        "sources": [
            [("code", "tmsh list sys ..."), ", ", ("code", "tmsh list ltm ...")],
            ["iControl REST, e.g. ", ("code", "/mgmt/tm/sys/sshd")],
            [("code", "bigip.conf"), " / ", ("code", "bigip_base.conf"), " from UCS backups"],
        ],
        "scope_notes": [
            ["State in ", ("b", "Comments"), " when a rule applies only to a module (ASM, APM) or only to specific partitions."],
            ["Note vCMP guest vs host applicability where it differs."],
        ],
        "example": [
            "F5-MGMT-001",
            "Restrict SSH management access",
            "MGMT",
            "SSH to the BIG-IP must be limited to approved management subnets.",
            [sev("HIGH")],
            [("code", "sys sshd allow"), " lists only approved management subnets; never ", ("code", "ALL")],
            [("code", "tmsh list sys sshd allow"), "; FAIL if ", ("code", "ALL"), " or any subnet not in the approved list"],
            [("code", "tmsh list sys sshd allow"), "; FAIL only if value is ", ("code", "ALL")],
            [auto("AUTOMATED")],
            "2026-09-30 / Reviewer name",
            "Approved subnet list is kept in the automation tool's variables file.",
        ],
        "remediation": "tmsh modify sys sshd allow replace-all-with { 10.10.0.0/24 }\ntmsh save sys config",
    },
    {
        "slug": "04-cisco-ios",
        "title": "MBSS – Routers & Switches – Cisco IOS",
        "short": "Cisco IOS",
        "category": "Routers & Switches",
        "product": "Cisco IOS and IOS-XE routers and switches",
        "versions": "e.g., IOS 15.2(x), IOS-XE 17.x",
        "prefix": "CSCO",
        "components": "Routers, L3 switches, L2 access switches",
        "sources": [
            [("code", "show running-config"), ", ", ("code", "show version"), ", ", ("code", "show ip ssh")],
            ["Parsed with regex, TextFSM or Genie (state which one in the rule detail)"],
        ],
        "scope_notes": [
            ["State in ", ("b", "Comments"), " when a rule applies only to routers, only to L3 switches or only to access switches."],
            ["Note rules that differ between IOS and IOS-XE syntax."],
        ],
        "example": [
            "CSCO-MGMT-001",
            "Allow only SSHv2 on VTY lines",
            "MGMT",
            "Remote management must use SSH version 2. Telnet must be disabled on all VTY lines.",
            [sev("HIGH")],
            [("code", "ip ssh version 2"), " and ", ("code", "transport input ssh"), " under every ", ("code", "line vty")],
            ["Parse ", ("code", "show running-config"), ": PASS if ", ("code", "ip ssh version 2"), " is present AND every ", ("code", "line vty"), " block has ", ("code", "transport input ssh"), " only"],
            ["Regex for ", ("code", "ip ssh version 2"), " only; VTY transport not checked"],
            [auto("AUTOMATED")],
            "2026-09-30 / Reviewer name",
            "Old check passed devices that still allowed Telnet on vty 5 15.",
        ],
        "remediation": "ip ssh version 2\nline vty 0 15\n transport input ssh",
    },
]


# ---------------------------------------------------------------- shared bits

def changelog_table():
    return (
        "table",
        ["Version", "Date", "Author", "Change", "Approved by"],
        [
            ["0.1", "YYYY-MM-DD", ph("Name"), "Initial draft from template", ph("Name")],
            [ph("x.y"), "YYYY-MM-DD", ph("Name"), ph("What changed"), ph("Name")],
        ],
    )


def status_legend():
    return [
        ("h", 3, "Severity"),
        (
            "table",
            ["Severity", "Meaning", "Target fix time (align with policy)"],
            [
                [[sev("CRITICAL")], "Direct path to compromise or outage", "e.g., 7 days"],
                [[sev("HIGH")], "Significant weakness in access, crypto or logging", "e.g., 30 days"],
                [[sev("MEDIUM")], "Hardening gap with limited direct exposure", "e.g., 90 days"],
                [[sev("LOW")], "Best practice or hygiene item", "e.g., next change window"],
            ],
        ),
        ("h", 3, "Automation status"),
        (
            "table",
            ["Status", "Meaning"],
            [
                [[auto("AUTOMATED")], "The automation tool checks the full requirement"],
                [[auto("PARTIAL")], "The tool checks part of the requirement. The gap is described in Comments"],
                [[auto("MANUAL")], "An engineer checks it during the review"],
                [[auto("PLANNED")], "Automation is in the backlog (see MBSS – Automation Backlog)"],
                [[auto("NOT FEASIBLE")], "Can't be verified from configuration or API output"],
            ],
        ),
    ]


# ---------------------------------------------------------------- pages

def overview_page():
    platform_rows = [
        [p["category"], p["product"], ph(p["versions"]), ph("count"), p["title"], ph("Team")]
        for p in PLATFORMS
    ]
    matrix_controls = [
        "Encrypted management only (SSH / HTTPS)",
        "Management access restricted (ACL / allow-list)",
        "Centralized AAA (TACACS+ / RADIUS)",
        "Local account password policy",
        "Remote syslog configured",
        "NTP from approved servers",
        "SNMPv3 only, no default communities",
        "Login warning banner",
        "Unused services disabled",
        "Approved software version",
        "Configuration backup",
    ]
    return [
        ("props", "mbss-overview", [
            ("Document owner", ph("Name / team")),
            ("Approver", ph("Name")),
            ("Version", "0.1"),
            ("Document status", [("st", "Grey", "DRAFT")]),
            ("Effective date", "YYYY-MM-DD"),
            ("Next review due", "YYYY-MM-DD"),
            ("Classification", ph("Internal / Confidential")),
        ]),
        ("toc", 2),
        ("h", 2, "Purpose"),
        ("p", ["This space defines the Minimum Baseline Security Standard (MBSS) for network devices. "
               "Each rule states the required configuration, how the Network Automation tool checks it today, "
               "and how the check has changed over time."]),
        ("h", 2, "Scope"),
        ("table", ["Category", "Vendor / product", "OS versions in scope", "Devices", "Page", "Owner team"], platform_rows),
        ("p", [("b", "Out of scope: "), ("ph", "List excluded device types, lab devices, etc.")]),
        ("h", 2, "How to read this standard"),
        *status_legend(),
        ("h", 2, "Coverage dashboard"),
        ("p", ["The report below reads the Page Properties table at the top of each platform page. "
               "Add the label ", ("code", "mbss-platform"), " to every platform page so it appears here."]),
        ("report", 'label = "mbss-platform" and space = currentSpace()',
         "Platform,Total rules,Automated rules,Automation coverage,Last full review,Next review due,Owner team"),
        ("expand", "Manual coverage table (use if the report macro is not available)", [
            ("table",
             ["Platform", "Total", "Automated", "Partial", "Manual", "Planned", "Not feasible", "Coverage %", "Last full review"],
             [[p["short"], "0", "0", "0", "0", "0", "0", "0%", "YYYY-MM-DD"] for p in PLATFORMS]),
        ]),
        ("h", 2, "Cross-vendor control matrix"),
        ("p", ["Enter the Rule ID for each platform, or N/A. Leave a cell empty only while the rule is still being written."]),
        ("table", ["Control"] + [p["short"] for p in PLATFORMS],
         [[c] + ["–"] * len(PLATFORMS) for c in matrix_controls]),
        ("h", 2, "Rule ID convention"),
        ("p", ["Format: ", ("code", "<PREFIX>-<DOMAIN>-<NNN>"), ", for example ", ("code", "CSCO-MGMT-001"),
               ". Prefixes: ", ("code", "CP"), " Check Point, ", ("code", "BC"), " BlueCoat, ",
               ("code", "F5"), " F5 BIG-IP, ", ("code", "CSCO"), " Cisco IOS. "
               "Rule IDs are never renumbered or reused."]),
        ("table", ["Domain code", "Domain", "Typical controls"],
         [[[("code", c)], n, t] for c, n, t in DOMAINS]),
        ("h", 2, "Review process"),
        ("ul", [
            [("b", "Scheduled review: "), ("ph", "quarterly"), ". Update Last Review on every rule you review, even if nothing changed."],
            [("b", "Also review after: "), "a major OS upgrade, a new CIS Benchmark release, a change to the automation tool's check logic, or an audit finding."],
            [("b", "When a check changes: "), "copy Current Check into Old Check, write the new logic in Current Check, and give the reason and date in Comments."],
            [("b", "Exceptions "), "go in MBSS – Exceptions & Waivers Register, not in the rule tables."],
        ]),
        ("h", 2, "Change log"),
        changelog_table(),
        ("h", 2, "References"),
        ("ul", [
            ["CIS Benchmarks (Cisco IOS, Check Point Firewall, F5 BIG-IP): https://www.cisecurity.org/cis-benchmarks"],
            ["Vendor hardening guides: ", ("ph", "add links")],
            ["Internal network security policy: ", ("ph", "add link")],
            ["Network Automation tool documentation / repository: ", ("ph", "add link")],
        ]),
    ]


def platform_page(p):
    pre = p["prefix"]
    example = [[c] if isinstance(c, str) else c for c in p["example"]]
    example[0] = [("b", p["example"][0]), ("br",), ("i", "EXAMPLE – delete")]
    blank = [
        ph(f"{pre}-DOMAIN-NNN"), ph("Short rule name"), ph("Domain code"),
        ph("What must be true"), ph("CRITICAL / HIGH / MEDIUM / LOW"),
        ph("Exact config / value that passes"), ph("Command or API + pass condition"),
        ph("Previous check logic, or N/A"), ph("AUTOMATED / PARTIAL / MANUAL / PLANNED / NOT FEASIBLE"),
        ph("YYYY-MM-DD / Name"), ph("Caveats, reason for check change, exception IDs"),
    ]
    detail_fields = [
        ("Applies to", ph("All / gateways only / routers only / ...")),
        ("Rationale / risk", ph("Why the rule exists; what happens if it is not met")),
        ("Automation check ID", ph("ID of the check in the automation tool")),
        ("Data source / command", ph("Command, API call or file the tool reads")),
        ("Parsing method", ph("Regex / TextFSM / Genie / JSON path")),
        ("Pass condition", ph("Exact condition")),
        ("Fail condition", ph("Exact condition")),
        ("Not applicable when", ph("e.g., feature not licensed or not configured")),
        ("Remediation impact", ph("None / session drop / service restart / reboot")),
        ("Auto-remediation allowed", ph("Yes / No / With change approval")),
        ("Reference", ph("CIS section, internal policy clause, NIST / ISO control")),
        ("Exceptions", ph("EXC-IDs, or None")),
        ("Why the check changed", ph("Old → current, with date and reason")),
    ]
    return [
        ("props", "mbss-platform", [
            ("Platform", f"{p['category']} – {p['short']}"),
            ("Vendor / product", p["product"]),
            ("OS versions in scope", ph(p["versions"])),
            ("Components in scope", p["components"]),
            ("Rule ID prefix", [("code", pre)]),
            ("Devices in scope", ph("count or link to inventory")),
            ("Total rules", "0"),
            ("Automated rules", "0"),
            ("Automation coverage", "0%"),
            ("Owner team", ph("Team")),
            ("Last full review", "YYYY-MM-DD"),
            ("Next review due", "YYYY-MM-DD"),
        ]),
        ("panel", "info", "How to maintain this page", [
            ("ul", [
                ["One row per rule in the Rule Register. Rule IDs are never renumbered or reused."],
                [("b", "Current Check"), ": the command or API the tool runs and the pass condition."],
                [("b", "When the tool's check changes"), ": move the text from Current Check to Old Check, "
                 "write the new logic in Current Check, give the reason and date in Comments, and update Last Review."],
                ["To retire a rule, strike through the row and write ", ("code", "RETIRED vX.Y"), " in Comments."],
                ["Update the counts in the table above after editing. The overview dashboard reads them."],
            ]),
        ]),
        ("toc", 2),
        ("h", 2, "Scope & applicability"),
        ("ul", [
            ["Components: " + p["components"]],
            *[["Data source: ", *s] for s in p["sources"]],
            *p["scope_notes"],
        ]),
        ("h", 2, "Rule register"),
        ("table", RULE_COLUMNS, [example, blank, [list(c) for c in blank]]),
        ("h", 2, "Rule details"),
        ("p", ["Optional. Copy this expand once per rule that needs more detail than the register holds."]),
        ("expand", f"{pre}-DOMAIN-NNN – Rule name – details", [
            ("table", ["Field", "Value"], [[[("b", k)], v] for k, v in detail_fields]),
            ("p", [("b", "Remediation (example syntax, verify before use):")]),
            ("code", p["remediation"]),
            ("p", [("b", "Review history")]),
            ("table", ["Date", "Reviewed by", "Outcome", "Notes"],
             [["YYYY-MM-DD", ph("Name"), ph("No change / check updated / rule updated"), ph("Notes")]]),
        ]),
        ("h", 2, "Known automation limitations & false positives"),
        ("table", ["Rule ID", "Limitation / false-positive scenario", "Impact", "Workaround", "Jira"],
         [[ph(f"{pre}-DOMAIN-NNN"), ph("What the tool gets wrong"), ph("Missed FAIL / false FAIL"), ph("Manual step"), ph("KEY-123")]]),
        ("h", 2, "Page change log"),
        changelog_table(),
    ]


def exceptions_page():
    return [
        ("panel", "note", "Before you add an exception", [
            ("ul", [
                ["Every exception needs an expiry date and a named risk owner."],
                ["Exclude the device from the automation tool's check for that rule, and record that in ", ("b", "Excluded in tool?"), "."],
                ["Put the Exception ID in the Comments column of the rule on its platform page."],
            ]),
        ]),
        ("h", 2, "Status"),
        ("table", ["Status", "Meaning"], [
            [[("st", "Green", "ACTIVE")], "Approved and within its expiry date"],
            [[("st", "Yellow", "EXPIRING")], "Expires within 30 days; renew or remediate"],
            [[("st", "Red", "EXPIRED")], "Past expiry; the device is non-compliant"],
            [[("st", "Grey", "CLOSED")], "Remediated or no longer needed"],
        ]),
        ("h", 2, "Register"),
        ("table",
         ["Exception ID", "Rule ID", "Platform", "Affected devices", "Business justification",
          "Compensating control", "Risk accepted by", "Approved on", "Expires on", "Excluded in tool?", "Status"],
         [[[("b", "EXC-001")], ph("CSCO-MGMT-001"), ph("Cisco IOS"), ph("Hostnames / group"), ph("Why it can't comply"),
           ph("What reduces the risk"), ph("Name, role"), "YYYY-MM-DD", "YYYY-MM-DD", ph("Yes / No"), [("st", "Green", "ACTIVE")]]]),
    ]


def backlog_page():
    return [
        ("p", ["Every rule whose Automation Status is PARTIAL, MANUAL or PLANNED has a row here."]),
        ("panel", "tip", "Jira", [
            ("p", ["If the work is tracked in Jira, add a Jira Issues macro below this panel filtered on the label ",
                   ("code", "mbss-automation"), "."]),
        ]),
        ("h", 2, "Backlog"),
        ("table",
         ["Rule ID", "Platform", "Current status", "Gap (why not fully automated)", "Proposed check",
          "Owner", "Target date", "Jira", "Progress"],
         [[ph("CP-POL-002"), ph("Check Point"), [auto("PARTIAL")], ph("e.g., inline layers not parsed"),
           ph("Command / API + logic"), ph("Name"), "YYYY-MM-DD", ph("KEY-123"), [("st", "Grey", "NOT STARTED")]]]),
        ("h", 2, "Progress status"),
        ("table", ["Status", "Meaning"], [
            [[("st", "Grey", "NOT STARTED")], "Not picked up"],
            [[("st", "Blue", "IN PROGRESS")], "Check being built or tested"],
            [[("st", "Green", "DONE")], "Live in the tool; platform page updated"],
        ]),
    ]


def all_pages():
    pages = [{
        "slug": "00-overview",
        "title": "Network MBSS",
        "tab": "Overview",
        "parent": None,
        "label": "mbss",
        "blocks": overview_page(),
    }]
    for p in PLATFORMS:
        pages.append({
            "slug": p["slug"],
            "title": p["title"],
            "tab": p["short"],
            "parent": "Network MBSS",
            "label": "mbss, mbss-platform",
            "blocks": platform_page(p),
        })
    pages.append({
        "slug": "05-exceptions",
        "title": "MBSS – Exceptions & Waivers Register",
        "tab": "Exceptions",
        "parent": "Network MBSS",
        "label": "mbss, mbss-exceptions",
        "blocks": exceptions_page(),
    })
    pages.append({
        "slug": "06-automation-backlog",
        "title": "MBSS – Automation Backlog",
        "tab": "Automation backlog",
        "parent": "Network MBSS",
        "label": "mbss, mbss-automation",
        "blocks": backlog_page(),
    })
    return pages
