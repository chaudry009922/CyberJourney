# Observations

## Devices Found

1. Windows Gateway
2. Kali Linux

---

## Security Observations

- Host discovery was successful.
- Gateway responded to Nmap but not to Ping.
- No open TCP ports were detected.
- Windows Firewall and WSL2 networking filtered all scanned ports.

---

## Analyst Notes

A host may ignore ICMP requests but still be reachable. Multiple tools should always be used during reconnaissance to avoid incorrect conclusions.