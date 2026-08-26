import pandas as pd


# CYBERTRAIL AI - BASIC THREAT ANALYZER

# Load dataset
df = pd.read_csv("data/sample_incident.csv")


print()
print("======================================")
print("          CYBERTRAIL AI")
print("   Autonomous Threat Investigation")
print("======================================")


# DATASET OVERVIEW

print()
print("DATASET OVERVIEW")
print("--------------------------------------")

print("Total events:", len(df))
print("Unique hosts:", df["hostname"].nunique())
print("Unique users:", df["user"].nunique())


# DETECT SUSPICIOUS DOMAINS

suspicious_domains = df[
    df["domain"]
    .fillna("")
    .str.contains("suspicious", case=False)
]


# DETECT SUSPICIOUS PROCESSES

suspicious_processes = df[
    df["process"]
    .fillna("")
    .str.lower()
    .isin(["powershell.exe", "cmd.exe"])
]


# DETECT EXTERNAL CONNECTIONS

external_connections = df[
    df["action"]
    .fillna("")
    .str.contains(
        "external|outbound",
        case=False,
        regex=True
    )
]


# FIND SUSPICIOUS HOSTS

suspicious_hosts = set()


for index, row in suspicious_domains.iterrows():
    suspicious_hosts.add(row["hostname"])


for index, row in suspicious_processes.iterrows():
    suspicious_hosts.add(row["hostname"])


for index, row in external_connections.iterrows():
    suspicious_hosts.add(row["hostname"])


# INVESTIGATION RESULTS

print()
print("INVESTIGATION RESULTS")
print("--------------------------------------")

print(
    "Suspicious domain events:",
    len(suspicious_domains)
)

print(
    "Suspicious process events:",
    len(suspicious_processes)
)

print(
    "External connection events:",
    len(external_connections)
)


print()
print("Suspicious Hosts:")


if suspicious_hosts:

    for host in suspicious_hosts:
        print("   ->", host)

else:

    print("   None detected")


# SHOW EVIDENCE

print()
print("EVIDENCE FOUND")
print("--------------------------------------")


# Suspicious DNS activity

if not suspicious_domains.empty:

    print()
    print("Suspicious DNS Activity:")

    print(
        suspicious_domains[
            [
                "timestamp",
                "hostname",
                "domain"
            ]
        ].to_string(index=False)
    )


# Suspicious process activity

if not suspicious_processes.empty:

    print()
    print("Suspicious Process Activity:")

    print(
        suspicious_processes[
            [
                "timestamp",
                "hostname",
                "process"
            ]
        ].to_string(index=False)
    )


# External network activity

if not external_connections.empty:

    print()
    print("External Network Activity:")

    print(
        external_connections[
            [
                "timestamp",
                "source_ip",
                "destination_ip",
                "hostname"
            ]
        ].to_string(index=False)
    )


# RISK CALCULATION

risk_score = (
    len(suspicious_domains)
    + len(suspicious_processes)
    + len(external_connections)
)


print()
print("======================================")


if risk_score >= 5:

    risk = "HIGH"

elif risk_score >= 2:

    risk = "MEDIUM"

else:

    risk = "LOW"


print("THREAT LEVEL:", risk)
print("Risk Score:", risk_score)

print("======================================")