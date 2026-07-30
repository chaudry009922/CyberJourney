# Day 03 – Networking Fundamentals and Network Discovery

## Objectives

- Understand networking basics.
- Learn IP addressing and subnetting.
- Understand TCP communication.
- Learn common ports and services.
- Discover devices on a network using Nmap.
- Analyze scan results like a SOC analyst.

---

## Theory

### DNS

DNS converts domain names into IP addresses.

Example:

google.com → 142.250.x.x

---

### IP Address

Every device on a network has an IP address.

Example:

172.29.89.170

---

### TCP

TCP establishes reliable communication using the Three-Way Handshake.

Client → SYN

Server → SYN-ACK

Client → ACK

---

### Ports

Ports allow multiple services to run simultaneously.

22 → SSH

80 → HTTP

443 → HTTPS

21 → FTP

53 → DNS

---

### Nmap

Nmap is used for:

- Host Discovery
- Port Scanning
- Service Detection
- Network Reconnaissance

---

## Commands Learned

ip addr

ip route

ping

nmap -sn

nmap -sV

---

## Lab Findings

Network:

172.29.80.0/20

Gateway:

172.29.80.1

Kali IP:

172.29.89.170

Hosts Found:

2

Open Ports:

None

Reason:

WSL2 virtual networking filters incoming traffic.

---

## Learning Outcome

Today I learned how devices communicate over a network, how to identify my subnet, discover live hosts using Nmap, and interpret service scan results.