import socket
import platform
import psutil
from datetime import datetime

print("=" * 50)
print("      NETWORK RECON DASHBOARD")
print("=" * 50)

print(f"Hostname           : {socket.gethostname()}")
print(f"Platform           : {platform.platform()}")
print(f"Python Version     : {platform.python_version()}")

print("\nNetwork Interfaces")

interfaces = psutil.net_if_addrs()

for interface, addresses in interfaces.items():
    print(f"\n{interface}")

    for addr in addresses:

        if addr.family == socket.AF_INET:
            print(f"  IPv4 : {addr.address}")

        elif str(addr.family) == "AddressFamily.AF_PACKET":
            print(f"  MAC  : {addr.address}")

print("\nCPU")

print(f"Physical Cores     : {psutil.cpu_count(False)}")
print(f"Logical Cores      : {psutil.cpu_count(True)}")
print(f"CPU Usage          : {psutil.cpu_percent(interval=1)} %")

memory = psutil.virtual_memory()

print("\nMemory")

print(f"Total RAM          : {memory.total/(1024**3):.2f} GB")
print(f"Available RAM      : {memory.available/(1024**3):.2f} GB")
print(f"Used               : {memory.percent} %")

disk = psutil.disk_usage('/')

print("\nDisk")

print(f"Total              : {disk.total/(1024**3):.2f} GB")
print(f"Used               : {disk.used/(1024**3):.2f} GB")
print(f"Free               : {disk.free/(1024**3):.2f} GB")

boot = datetime.fromtimestamp(psutil.boot_time())

print("\nBoot Time")

print(boot)

print("\nCurrent Time")

print(datetime.now())

print("=" * 50)