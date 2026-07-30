# Lab 03 – Network Discovery

## Objective

Perform basic network reconnaissance using Linux networking tools and Nmap.

---

## Commands Used

ip addr

ip route

ping 172.29.80.1

nmap -sn 172.29.80.0/20

nmap -sV 172.29.89.170

nmap -sV 172.29.80.1

---

## Results

Host Discovery

- 172.29.80.1
- 172.29.89.170

Port Scan

No open ports were detected.

All scanned ports were filtered.

---

## Conclusion

This lab demonstrated basic network discovery and service detection. Because Kali is running inside WSL2, Windows networking filters incoming traffic, resulting in no accessible TCP services.