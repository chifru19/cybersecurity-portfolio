import requests
import sys

def scan_target(url):
    print(f"\n[*] Scanning target: {url}\n" + "-"*40)
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"[!] Error connecting to target: {e}")
        return

    # 1. Check Security Headers
    headers_to_check = {
        "Content-Security-Policy": "Protects against XSS and data injection",
        "X-Frame-Options": "Protects against Clickjacking",
        "X-Content-Type-Options": "Prevents MIME-type sniffing",
        "Strict-Transport-Security": "Enforces HTTPS connections"
    }

    print("[+] Checking HTTP Security Headers:")
    for header, description in headers_to_check.items():
        if header in response.headers:
            print(f"    [SECURE] {header} is present.")
        else:
            print(f"    [WARNING] Missing {header} ({description})")

    # 2. Check Sensitive Files/Paths
    sensitive_paths = [".git/config", ".env", "config.json", "backup.zip"]
    print("\n[+] Checking for Exposed Sensitive Files:")
    for path in sensitive_paths:
        test_url = f"{url.rstrip('/')}/{path}"
        try:
            res = requests.get(test_url, timeout=3)
            if res.status_code == 200:
                print(f"    [CRITICAL] Exposed file found: {test_url}")
            else:
                print(f"    [SAFE] Not found: {path}")
        except Exception:
            pass
    print("-" * 40 + "\n[+] Scan completed!\n")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8501"
    scan_target(target)
