# Day 01 – Linux Fundamentals & Environment Setup

**Date:** July 28, 2026

## Objective

Set up the cybersecurity development environment and learn the fundamental Linux commands required for future cybersecurity labs.

---

## Topics Covered

- Linux directory structure
- Terminal navigation
- Creating and managing files
- Copying, moving, and deleting files
- Viewing file contents
- Searching for files
- Searching text inside files
- Basic Linux file permissions
- Git version control basics

---

## Commands Practiced

```bash
pwd
ls
ls -l
ls -la
cd
mkdir
touch
cp
mv
rm
cat
echo
find
grep
```

---

## Key Concepts Learned

### Linux Root Directory

Linux starts from a single root directory:

```
/
```

Unlike Windows, all directories branch from this root.

---

### Important Directories

| Directory | Purpose |
|-----------|---------|
| `/` | Root directory |
| `/home` | User files |
| `/var/log` | System log files |
| `/etc` | Configuration files |
| `/usr` | Installed software |

---

### File Operations

- `cp` copies files.
- `mv` moves or renames files.
- `rm` deletes files.
- `touch` creates empty files.

---

### Output Redirection

`>` overwrites a file.

Example:

```bash
echo "Hello" > file.txt
```

`>>` appends to a file.

Example:

```bash
echo "World" >> file.txt
```

---

### Searching

Find files:

```bash
find ~/CyberJourney -name "*.txt"
```

Search inside files:

```bash
grep "Python" skills.txt
```

---

## Lab Activities Completed

- Created Day01 lab directory
- Practiced Linux navigation
- Created and managed files
- Used search commands
- Explored Linux permissions
- Initialized Git repository
- Connected GitHub using SSH

---

## Challenges Faced

- Accidentally used `cd ...` instead of `cd ..`
- Learned that `...` is not a valid directory shortcut.
- Learned that Linux is case-sensitive.

---

## Key Takeaways

- Linux commands are simple but powerful.
- Reading terminal error messages helps solve problems.
- Understanding the Linux filesystem is essential before learning cybersecurity tools.

---

## Next Steps

- Linux processes
- File permissions
- Bash scripting
- System monitoring
- Python automation for cybersecurity

---

## Repository

CyberJourney

Day completed successfully.
