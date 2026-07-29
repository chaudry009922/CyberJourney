import os
import platform
import socket
from datetime import datetime
import psutil

def display_system_info():
    print("=" * 40)
    print("       SYSTEM INFORMATION DASHBOARD")
    print("=" * 40)

    
    try:
        current_user = os.getlogin()
    except Exception:
        import getpass
        current_user = getpass.getuser()
    print(f"Current User:           {current_user}")

    # Hostname
    print(f"Hostname:               {socket.gethostname()}")

    # Current working directory
    print(f"Current Working Dir:    {os.getcwd()}")

    # Linux kernel version / System platform
    print(f"Kernel / OS Version:    {platform.platform()}")
    print(f"Python Version:         {platform.python_version()}")

    # CPU information
    print(f"CPU Cores (Physical):   {psutil.cpu_count(logical=False)}")
    print(f"CPU Cores (Total):      {psutil.cpu_count(logical=True)}")
    print(f"CPU Usage:              {psutil.cpu_percent(interval=1)}%")

    # Memory information
    mem = psutil.virtual_memory()
    print(f"Total Memory:           {mem.total / (1024**3):.2f} GB")
    print(f"Available Memory:       {mem.available / (1024**3):.2f} GB ({mem.percent}% used)")

    # Disk usage (Root directory)
    disk = psutil.disk_usage('/')
    print(f"Total Disk Space:       {disk.total / (1024**3):.2f} GB")
    print(f"Disk Usage:             {disk.used / (1024**3):.2f} GB ({disk.percent}%)")

    # IP addresses
    print("IP Addresses:")
    interfaces = psutil.net_if_addrs()
    for interface_name, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                print(f"  - {interface_name}: {addr.address}")

    # Current system time
    print(f"Current System Time:    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 40)

if __name__ == "__main__":
    display_system_info()