import pandas as pd

from tools import (
    dns_investigation,
    endpoint_investigation,
    network_investigation,
    timeline_investigation
)


class CyberTrailAgent:

    def __init__(self, df):
        self.df = df
        self.findings = []
        self.score = 0

    def investigate(self):

        print("\n" + "=" * 60)
        print("CYBERTRAIL AI - AUTONOMOUS INVESTIGATION")
        print("=" * 60)

        # Step 1: DNS investigation
        print("\n[AGENT] Checking DNS activity...")

        dns_results = dns_investigation(self.df)

        if not dns_results.empty:
            self.findings.append(
                "Suspicious DNS activity detected."
            )
            self.score += 25

            print(
                "[AGENT] Suspicious DNS activity found."
            )
        else:
            print(
                "[AGENT] No suspicious DNS activity found."
            )

        # Step 2: Endpoint investigation
        print("\n[AGENT] Checking endpoint processes...")

        endpoint_results = endpoint_investigation(self.df)

        if not endpoint_results.empty:
            self.findings.append(
                "Suspicious endpoint processes detected."
            )
            self.score += 25

            print(
                "[AGENT] Suspicious processes found."
            )
        else:
            print(
                "[AGENT] No suspicious endpoint processes found."
            )

        # Step 3: Network investigation
        print("\n[AGENT] Checking network activity...")

        network_results = network_investigation(self.df)

        suspicious_network = network_results[
            network_results["action"]
            .str.contains(
                "external|outbound|internal",
                case=False,
                na=False
            )
        ]

        if not suspicious_network.empty:
            self.findings.append(
                "Suspicious network communication detected."
            )
            self.score += 25

            print(
                "[AGENT] Suspicious network activity found."
            )
        else:
            print(
                "[AGENT] No suspicious network activity found."
            )

        # Step 4: Timeline investigation
        print("\n[AGENT] Reconstructing event timeline...")

        timeline = timeline_investigation(self.df)

        print(
            "[AGENT] Timeline reconstructed successfully."
        )

        # Step 5: Identify affected host
        suspicious_hosts = []

        if not dns_results.empty:
            suspicious_hosts.extend(
                dns_results["hostname"].dropna().tolist()
            )

        if not endpoint_results.empty:
            suspicious_hosts.extend(
                endpoint_results["hostname"].dropna().tolist()
            )

        if not suspicious_network.empty:
            suspicious_hosts.extend(
                suspicious_network["hostname"].dropna().tolist()
            )

        if suspicious_hosts:

            host_counts = pd.Series(
                suspicious_hosts
            ).value_counts()

            affected_host = host_counts.index[0]

        else:
            affected_host = "No suspicious host identified"

        # Step 6: Risk assessment
        if self.score >= 75:
            risk = "HIGH"
        elif self.score >= 50:
            risk = "MEDIUM"
        elif self.score >= 25:
            risk = "LOW"
        else:
            risk = "MINIMAL"

        # Final report
        print("\n" + "=" * 60)
        print("INVESTIGATION RESULT")
        print("=" * 60)

        print(
            f"\nAffected Host: {affected_host}"
        )

        print(
            f"Risk Level: {risk}"
        )

        print(
            f"Risk Score: {self.score}/100"
        )

        print("\nEvidence:")

        for finding in self.findings:
            print(f"- {finding}")

        print("\nAttack Timeline:")

        for _, row in timeline.iterrows():

            print(
                f"{row['timestamp']} | "
                f"{row['hostname']} | "
                f"{row['event_type']} | "
                f"{row['action']}"
            )

        print("\n" + "=" * 60)

        return {
            "affected_host": affected_host,
            "risk_level": risk,
            "risk_score": self.score,
            "findings": self.findings,
            "timeline": timeline
        }


if __name__ == "__main__":

    df = pd.read_csv(
        "data/sample_incident.csv"
    )

    agent = CyberTrailAgent(df)

    agent.investigate()