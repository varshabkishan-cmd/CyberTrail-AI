import pandas as pd


def dns_investigation(df):
    suspicious_domains = df[
        df["domain"]
        .fillna("")
        .str.contains(
            "suspicious|malicious|evil|attack",
            case=False,
            regex=True
        )
    ]

    return suspicious_domains[
        [
            "timestamp",
            "hostname",
            "user",
            "domain",
            "action"
        ]
    ]


def endpoint_investigation(df):
    suspicious_processes = df[
        df["process"]
        .fillna("")
        .str.lower()
        .isin(
            [
                "powershell.exe",
                "cmd.exe",
                "wscript.exe",
                "cscript.exe"
            ]
        )
    ]

    return suspicious_processes[
        [
            "timestamp",
            "hostname",
            "user",
            "process",
            "action"
        ]
    ]


def network_investigation(df):
    network_events = df[
        df["action"]
        .fillna("")
        .str.contains(
            "external|outbound|connection",
            case=False,
            regex=True
        )
    ]

    return network_events[
        [
            "timestamp",
            "source_ip",
            "destination_ip",
            "hostname",
            "action"
        ]
    ]


def timeline_investigation(df):
    timeline = df.copy()

    timeline["timestamp"] = pd.to_datetime(
        timeline["timestamp"],
        errors="coerce"
    )

    timeline = timeline.sort_values(
        by="timestamp"
    )

    return timeline[
        [
            "timestamp",
            "hostname",
            "user",
            "event_type",
            "process",
            "domain",
            "action"
        ]
    ]