from pathlib import Path

BASE_DIR = Path(__file__).parent
log_file = BASE_DIR / "logs" / "sample.log"

info = 0
warning = 0
error = 0

with open(log_file, "r") as file:
    logs = file.readlines()

for line in logs:

    if line.startswith("INFO"):
        info += 1

    elif line.startswith("WARNING"):
        warning += 1

    elif line.startswith("ERROR"):
        error += 1

print("=" * 40)
print("SentinelAI Log Summary")
print("=" * 40)

print(f"Total Logs : {len(logs)}")
print(f"INFO       : {info}")
print(f"WARNING    : {warning}")
print(f"ERROR      : {error}")

print("\nFirst Log:")
print(logs[0].strip())

print("\nLast Log:")
print(logs[-1].strip())