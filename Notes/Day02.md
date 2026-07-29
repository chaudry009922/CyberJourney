# Day 02 - Linux Permissions, Processes, Logs & System Information

**Date:** July 29, 2026

## Objective

The objective of Day 2 was to gain practical experience with Linux system administration concepts that are essential for cybersecurity and SOC analysts. The lab focused on file permissions, process management, log analysis, and creating a Python-based system information collector.

---

## Topics Covered

* Linux File Permissions
* Linux Processes
* Linux System Logs
* Basic System Investigation
* Python Automation
* Git & GitHub Workflow

---

## Linux Commands Practiced

### File Permissions

```bash
chmod 777 notes.txt
chmod 644 notes.txt
chmod +x script.sh
```

**Learned:**

* Read (r) = 4
* Write (w) = 2
* Execute (x) = 1
* Difference between permission values such as 777 and 644.
* Making a shell script executable.

---

### Process Management

```bash
ps
ps aux
top
pgrep bash
```

**Learned:**

* Viewing running processes.
* Monitoring CPU and memory usage.
* Finding specific processes.
* Understanding how Linux manages active programs.

---

### System Information

```bash
whoami
hostname
uname -a
ip addr
pwd
```

**Learned:**

* Current logged-in user.
* Hostname of the system.
* Linux kernel version.
* Network interface information.
* Current working directory.

---

### Log Analysis

```bash
cd /var/log
ls
head dpkg.log
tail dpkg.log
grep install dpkg.log
find /var/log -type f
```

**Learned:**

* Location of important Linux log files.
* Using grep to search logs.
* Viewing recent installation history.
* Understanding "Permission Denied" messages during investigations.

---

## Python Mini Project

Created a Python application named:

```text
Python/system_info.py
```

The application displays:

* Current User
* Hostname
* Current Working Directory
* Linux Kernel Version
* Python Version
* CPU Information
* Memory Usage
* Disk Usage
* Network Interfaces
* Current System Time

The project uses the following Python modules:

* os
* platform
* socket
* datetime
* psutil

This was my first practical Linux automation tool.

---

## Challenges Faced

* Encountered permission errors while searching protected directories.
* Learned that some Linux directories require root privileges.
* Faced issues installing Python packages due to Kali's PEP 668 protection.
* Learned that virtual environments are the recommended solution for Python development.

---

## Key Takeaways

* Linux permissions are fundamental to system security.
* Every running application is a process that can be monitored.
* Log files are one of the primary sources of evidence during cybersecurity investigations.
* Python can automate system information gathering and reduce manual work.
* Git and GitHub should be used to document learning consistently.

---

## Commands I Need to Remember

```bash
pwd
ls -l
chmod
ps
ps aux
top
pgrep
whoami
hostname
uname -a
ip addr
grep
find
head
tail
git add .
git commit -m "message"
git push origin main
```

---

## Reflection

Today was my first step toward learning Linux from a cybersecurity perspective instead of just using it as an operating system. I learned how permissions, processes, and logs work together and built a Python tool to collect system information automatically. These concepts form the foundation for future SOC investigations, network analysis, and automation projects.

**Status:** ✅ Completed Day 2 Successfully
