"""Write this machine's public IP to ip.txt and optionally copy it to a server.

Set DEPLOY_HOST (e.g. user@server) to copy ip.txt with scp after each change.
Authentication uses your SSH key; no passwords are stored here.
"""
import os
import subprocess
import time

from requests import get

DEPLOY_HOST = os.environ.get("DEPLOY_HOST")
DEPLOY_PATH = os.environ.get("DEPLOY_PATH", "~/deepdream/")


def public_ip():
    return get("https://api.ipify.org", timeout=10).text.strip()


def publish(ip):
    with open("ip.txt", "w") as f:
        f.write(ip)
    if DEPLOY_HOST:
        subprocess.run(["scp", "ip.txt", f"{DEPLOY_HOST}:{DEPLOY_PATH}"], check=False)
    print(f"ip: {ip}")


ip = public_ip()
publish(ip)

while True:
    try:
        current = public_ip()
        if current != ip:
            ip = current
            publish(ip)
    except Exception:
        print("Network error")
    time.sleep(5)
