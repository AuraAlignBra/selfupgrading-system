#!/usr/bin/env python3
import sys, os, subprocess, time, requests

GITHUB_USER = "AuraAlignBra"
REPO_NAME = "selfupgrading-system"
VERSION_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/version.txt"
SCRIPT_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/selfupgrade.py"

def get_version():
    try:
        r = requests.get(VERSION_URL, timeout=5)
        return r.text.strip() if r.status_code == 200 else "0"
    except: return "0"

def update():
    try:
        r = requests.get(SCRIPT_URL, timeout=10)
        if r.status_code == 200 and "html" not in r.text[:50].lower():
            with open(__file__, "w") as f:
                f.write(r.text)
            os.chmod(__file__, 0o755)
            print("✅ Updated! Restarting...")
            time.sleep(1)
            subprocess.Popen([sys.executable, __file__])
            sys.exit(0)
    except: pass

def main():
    print("🤖 AuraAlignBra System Active")
    remote = get_version()
    local = "1.0"
    if remote and remote > local:
        print("🔄 Updating...")
        update()
    print("💚 System healthy - Press Ctrl+C to stop")
    while True:
        print(f"[{time.strftime('%H:%M:%S')}] Heartbeat - Alive")
        time.sleep(60)

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: print("\n👋 Shutdown")

