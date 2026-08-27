import pandas as pd

from tools import (
    dns_investigation,
    endpoint_investigation,
    network_investigation,
    timeline_investigation
)


df = pd.read_csv(
    "data/sample_incident.csv"
)


print("DNS INVESTIGATION")
print(dns_investigation(df))


print()
print("ENDPOINT INVESTIGATION")
print(endpoint_investigation(df))


print()
print("NETWORK INVESTIGATION")
print(network_investigation(df))


print()
print("TIMELINE")
print(timeline_investigation(df))