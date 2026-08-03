import socket
from datetime import datetime

print("=" * 50)
print("      CUSTOM PORT SCANNER")
print("=" * 50)

target = input("Enter Target IP: ")

ports = [
    20,
    21,
    22,
    23,
    25,
    53,
    80,
    110,
    143,
    443,
    445,
    3389
]

print(f"\nScanning {target}")
print(f"Started : {datetime.now()}\n")

for port in ports:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN ] Port {port}")

    else:
        print(f"[CLOSED] Port {port}")

    sock.close()

print("\nScan Complete")