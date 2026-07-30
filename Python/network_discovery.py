import subprocess

print("=" * 50)
print("        SentinelAI - Network Discovery")
print("=" * 50)

network = input("Enter network (Example: 172.29.80.0/20): ")

print("\nScanning network...\n")

try:
    result = subprocess.run(
        ["nmap", "-sn", network],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    with open("../Labs/Day03/network_scan.txt", "w") as file:
        file.write(result.stdout)

    print("\nScan report saved successfully.")

except Exception as e:
    print("Error:", e)

print("=" * 50)