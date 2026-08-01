# Day 05 – Passive Web Reconnaissance & Python Web Recon Scanner

**Date:** 02 August 2026

---

# Objective

The objective of today's lab was to understand the reconnaissance phase of penetration testing and build a Python tool capable of gathering basic information about a website.

Reconnaissance is the first stage of every penetration test. Before attempting to identify vulnerabilities, a security professional gathers publicly available information about the target.

---

# Theory

## What is Reconnaissance?

Reconnaissance (Recon) is the process of collecting information about a target before performing any security assessment.

There are two types of reconnaissance:

### Passive Reconnaissance

Passive reconnaissance gathers information without directly interacting with the target in an intrusive manner.

Examples:

- DNS Lookup
- WHOIS
- HTTP Headers
- robots.txt
- security.txt
- Google Dorking
- Public Certificates

Passive recon is generally safe and is often allowed by bug bounty programs.

---

### Active Reconnaissance

Active reconnaissance directly communicates with the target.

Examples:

- Nmap Scanning
- Port Scanning
- Service Enumeration
- Directory Brute Force
- Vulnerability Scanning

Active recon should only be performed on systems you own or where you have explicit authorization.

---

# HTTP Request Flow

```
Browser
      ↓
DNS Resolution
      ↓
IP Address
      ↓
TCP Connection
      ↓
HTTP Request
      ↓
Web Server
      ↓
HTTP Response
```

Every website follows this communication process.

---

# Linux Commands Used

## Create Day 5 Lab

```bash
mkdir -p Labs/Day05
touch Labs/Day05/recon_notes.md
touch Labs/Day05/commands.txt
touch Labs/Day05/report.md
```

---

## DNS Lookup

```bash
nslookup example.com
```

Purpose:

Resolve a domain name into one or more IP addresses.

---

## Ping Test

```bash
ping -c 4 example.com
```

Purpose:

Check network connectivity and measure latency.

---

## Retrieve HTTP Headers

```bash
curl -I https://example.com
```

Purpose:

Display only the HTTP response headers without downloading the webpage.

---

## Retrieve robots.txt

```bash
curl https://example.com/robots.txt
```

Purpose:

Check whether the website exposes a robots.txt file that lists restricted directories.

---

## Retrieve security.txt

```bash
curl https://example.com/.well-known/security.txt
```

Purpose:

Check whether the organization publishes vulnerability disclosure information.

---

# Lab Observations

## DNS

The domain resolved successfully.

Multiple IP addresses were returned because the website uses Cloudflare.

---

## Ping

Packets Sent: 4

Packets Received: 4

Packet Loss: 0%

Average Latency: Approximately 36 ms

The host was reachable.

---

## HTTP Headers

Status Code:

200 OK

Server:

Cloudflare

Content-Type:

text/html

Observation:

The website is protected by Cloudflare and serves HTML content successfully.

---

## robots.txt

The requested file was not available.

Instead, the server returned the default webpage.

---

## security.txt

The server returned the default webpage instead of a dedicated security.txt file.

---

# Python Project

Project Name:

Web Recon Scanner v1

Purpose:

Automate the collection of basic reconnaissance information about a website.

Current Features:

- Accept website input
- Resolve IP Address
- Send HTTP Request
- Display Response Time
- Display HTTP Headers
- Display Status Code

Python Libraries Used

- socket
- requests
- time

---

# Skills Learned

- Passive Reconnaissance
- DNS Resolution
- HTTP Requests
- HTTP Response Headers
- Python Networking
- Virtual Environment Management
- Installing Python Packages
- Basic Automation

---

# Future Improvements

Version 2 will include:

- WHOIS Lookup
- SSL Certificate Information
- DNS Record Enumeration
- Security Header Analysis
- Markdown Report Generation
- Automatic Risk Summary

---

# Conclusion

Today's lab introduced the fundamentals of passive reconnaissance and demonstrated how Python can automate common information-gathering tasks.

The Web Recon Scanner serves as the foundation for future reconnaissance and penetration testing projects.