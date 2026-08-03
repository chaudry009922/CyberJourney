import socket
import requests
import time


def banner():
    print("=" * 50)
    print("        WEB RECON SCANNER")
    print("=" * 50)


def resolve_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return "Unable to resolve"


def get_headers(url):
    try:
        start = time.time()

        response = requests.get(url, timeout=5)

        end = time.time()

        print(f"\nStatus Code : {response.status_code}")
        print(f"Response Time : {(end-start)*1000:.2f} ms\n")

        print("Headers\n")

        for key, value in response.headers.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(e)


banner()

target = input("Enter Website (example.com): ")

if not target.startswith("http"):
    url = "https://" + target
else:
    url = target

print("\nResolving IP...")

ip = resolve_ip(target.replace("https://","").replace("http://",""))

print("IP Address :", ip)

get_headers(url)

important_headers = [

"Content-Security-Policy",

"X-Frame-Options",

"Strict-Transport-Security",

"Referrer-Policy",

"Permissions-Policy"

]

print("\nSecurity Headers")

for h in important_headers:

    if h in response.headers:

        print(f"[FOUND] {h}")

    else:

        print(f"[MISSING] {h}")