# Day 04 – Network Reconnaissance & Python Automation

## Objective

Today's objective was to understand reconnaissance (Recon), perform basic network discovery using Linux and Nmap, and begin building Python automation tools useful for cybersecurity.

---

# Theory

## What is Reconnaissance?

Reconnaissance is the first phase of a penetration test where information is collected about a target before attempting exploitation.

The better the reconnaissance, the easier it becomes to identify potential attack surfaces.

Recon is also important for SOC Analysts because suspicious scanning activity is often one of the first indicators of an attack.

---

## Types of Recon

### Passive Recon

Information gathering without directly interacting with the target.

Examples:
- Google Dorking
- WHOIS Lookup
- DNS Records
- LinkedIn
- GitHub

Advantages:
- Difficult to detect
- No interaction with target

---

### Active Recon

Information gathering through direct interaction.

Examples:
- Ping
- Nmap
- Banner Grabbing
- Port Scanning

Advantages:
- More accurate information

Disadvantages:
- Can be detected by firewalls or IDS.

---

# Commands Practiced

| Command | Purpose |
|----------|----------|
| ip addr | Display network interfaces and IP addresses |
| ip route | Display routing table |
| hostname | Show system hostname |
| hostname -I | Display assigned IP address |
| ping | Check network connectivity |
| nmap -sn | Discover live hosts |
| nmap -sV | Detect services running on open ports |
| nmap -O | Attempt Operating System detection |

---

# Lab Findings

## Network Information

Hostname:
DESKTOP-N7NP5CC

Local IP:
172.29.89.170

Gateway:
172.29.80.1

Subnet:
172.29.80.0/20

---

## Ping Result

Ping to gateway returned 100% packet loss.

Possible Reason:
WSL2 networking blocks ICMP replies from the virtual gateway even though the gateway exists.

---

## Host Discovery

Command:

nmap -sn 172.29.80.0/20

Result:

2 Hosts Found

Host 1:
172.29.80.1

Host 2:
172.29.89.170

---

## Service Detection

Command:

nmap -sV 172.29.89.170

Result:

No open ports detected.

1000 TCP ports were filtered.

Possible Reason:

Windows Firewall or WSL networking filters incoming packets.

---

## OS Detection

Command:

nmap -O 172.29.89.170

Result:

Unable to accurately identify the operating system because all ports were filtered.

---

# Key Learning

Reconnaissance is the foundation of every penetration test.

Nmap can discover:

- Live Hosts
- Open Ports
- Services
- Operating Systems

Firewalls can prevent service detection and OS fingerprinting.

A SOC Analyst should recognize repeated scanning activity as potential reconnaissance.

---

# Reflection

Today's lab demonstrated how reconnaissance works in practice.

Although no open ports were found due to WSL networking and firewall restrictions, the exercise helped build confidence with Nmap, Linux networking commands, and interpreting scan results.