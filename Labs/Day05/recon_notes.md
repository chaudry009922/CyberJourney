# Day 05 – Reconnaissance Notes

# What is Reconnaissance?

Reconnaissance (Recon) is the first phase of penetration testing. It involves collecting information about a target before attempting to identify vulnerabilities or perform any security testing.

The primary goal is to understand the target's infrastructure, technologies, and publicly available information while minimizing unnecessary interaction.

---

# Types of Reconnaissance

## 1. Passive Reconnaissance

Passive reconnaissance gathers information without directly attacking or interacting aggressively with the target.

Examples:

- DNS Lookup
- WHOIS Lookup
- HTTP Header Inspection
- robots.txt
- security.txt
- Google Dorking
- Certificate Transparency Logs
- Public GitHub Repositories

Advantages:

- Difficult to detect
- Safe for learning
- Usually permitted in bug bounty programs

---

## 2. Active Reconnaissance

Active reconnaissance directly communicates with the target system.

Examples:

- Nmap Port Scanning
- Service Enumeration
- Banner Grabbing
- Directory Enumeration
- Vulnerability Scanning

Advantages:

- More detailed information

Disadvantages:

- Can generate logs
- May trigger security alerts
- Requires authorization

---

# Reconnaissance Workflow

```
Choose Target
      │
      ▼
DNS Lookup
      │
      ▼
Resolve IP Address
      │
      ▼
Check Connectivity
      │
      ▼
Collect HTTP Headers
      │
      ▼
Inspect robots.txt
      │
      ▼
Inspect security.txt
      │
      ▼
Record Findings
```

---

# Commands Used

## DNS Lookup

```bash
nslookup example.com
```

Purpose:

Find the IP address associated with a domain name.

---

## Connectivity Test

```bash
ping -c 4 example.com
```

Purpose:

Verify whether the host is reachable and measure network latency.

---

## HTTP Headers

```bash
curl -I https://example.com
```

Purpose:

Retrieve HTTP response headers without downloading the webpage content.

---

## robots.txt

```bash
curl https://example.com/robots.txt
```

Purpose:

Determine whether the website publishes crawler restrictions or sensitive paths.

---

## security.txt

```bash
curl https://example.com/.well-known/security.txt
```

Purpose:

Check whether the organization provides vulnerability disclosure or security contact information.

---

# Results

## Target

example.com

---

## DNS Resolution

Successfully resolved the domain to an IPv4 address.

Observed Address:

172.66.147.243

---

## Ping

Packets Sent: 4

Packets Received: 4

Packet Loss: 0%

Average Response Time: ~36 ms

The target was reachable.

---

## HTTP Headers

Status Code:

200 OK

Server:

Cloudflare

Content-Type:

text/html

Observation:

The website is protected by Cloudflare and responded successfully.

---

## robots.txt

No dedicated robots.txt file was returned.

The default webpage was displayed instead.

---

## security.txt

No dedicated security.txt file was found.

The default webpage was returned.

---

# Key Findings

- DNS resolution was successful.
- The website was reachable.
- Cloudflare protects the target.
- HTTP requests returned status code 200.
- No public robots.txt was identified.
- No public security.txt was identified.
- Passive reconnaissance was completed without performing intrusive actions.

---

# Skills Practiced

- DNS Resolution
- Host Reachability Testing
- HTTP Header Analysis
- Website Fingerprinting
- Passive Reconnaissance
- Linux Networking Commands
- Documentation of Security Findings

---

# Conclusion

Passive reconnaissance provides valuable information about a target while minimizing interaction. During this lab, DNS information, network connectivity, HTTP headers, and publicly accessible security-related files were examined. These findings form the foundation for later phases of an authorized penetration test or security assessment.