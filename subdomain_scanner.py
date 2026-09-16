import sys
import requests
import socket
from concurrent.futures import ThreadPoolExecutor

def query_crtsh(target):
    url = f"https://crt.sh/?q=%25.{target}&output=json"
    subdomains = set()
    try:
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            data = res.json()
            for entry in data:
                name_value = entry.get('name_value', '')
                for sub in name_value.split('\n'):
                    sub = sub.strip()
                    if sub and '*' not in sub:
                        subdomains.add(sub)
    except Exception as e:
        print(f"    [ERROR] CRT.sh query failed: {e}")
    return sorted(list(subdomains))

def resolve_subdomain(sub):
    try:
        ip = socket.gethostbyname(sub)
        print(f"    [ACTIVE] {sub} -> {ip}")
    except socket.gaierror:
        pass

def run_enumeration(target):
    print(f"\n[*] Enumerating subdomains for: {target}")
    print("-" * 50)
    subs = query_crtsh(target)
    if not subs:
        print("    [INFO] No subdomains found via public records.")
        return
        
    print(f"[*] Found {len(subs)} unique subdomains. Resolving active hosts...")
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(resolve_subdomain, subs)
    print("-" * 50 + "\n[+] Subdomain enumeration completed!\n")

if __name__ == "__main__":
    domain = sys.argv[1] if len(sys.argv) > 1 else "frankfru.com"
    run_enumeration(domain)
