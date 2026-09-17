import subprocess
import os

TARGET_DOMAIN = "frankfru.com"
TARGET_URL = "https://frankfru.com"

if not os.path.exists("sample_access.log"):
    with open("sample_access.log", "w") as f:
        f.write('192.168.1.1 - - [17/Sep/2026:10:00:00 +0000] "GET /admin HTTP/1.1" 403 512\n')
        f.write('10.0.0.5 - - [17/Sep/2026:10:01:00 +0000] "GET /wp-login.php HTTP/1.1" 200 1024\n')

execution_plan = [
    ("1/13 | Web App Vulnerability Scan", ["python3", "scanner.py", TARGET_URL]),
    ("2/13 | Log Analysis & Threat Detection", ["python3", "log_analyzer.py", "sample_access.log"]),
    ("3/13 | Encrypted File Share Test", ["python3", "file_encryptor.py"]),
    ("4/13 | Automated Secret Scan", ["python3", "secret_scanner.py"]),
    ("5/13 | Network Port Scan", ["python3", "port_scanner.py", TARGET_DOMAIN]),
    ("6/13 | Phishing Awareness Simulator", ["python3", "phishing_simulator.py"]),
    ("7/13 | JWT Security Auditor", ["python3", "jwt_auditor.py"]),
    ("8/13 | SSL/TLS Certificate Inspector", ["python3", "ssl_checker.py", TARGET_DOMAIN]),
    ("9/13 | Password Strength / HIBP Check", ["python3", "password_checker.py"]),
    ("10/13 | Subdomain Enumerator (CRT.sh)", ["python3", "subdomain_scanner.py", TARGET_DOMAIN]),
    ("11/13 | AWS S3 Bucket Exposure Audit", ["python3", "s3_auditor.py", TARGET_DOMAIN]),
    ("12/13 | Threat Intel & IP Lookup", ["python3", "threat_intel.py", TARGET_DOMAIN]),
    ("13/13 | Master Inventory Summary", ["python3", "portfolio_dashboard.py"]),
]

def run_suite():
    print(f"[*] Starting Full 13-Module Security Audit against {TARGET_DOMAIN}...\n" + "="*60)
    for title, cmd in execution_plan:
        print(f"\n>>> [{title}] Command: {' '.join(cmd)}")
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=12)
            output = res.stdout.strip() or res.stderr.strip()
            print(output if output else "[*] Executed (silent/interactive exit 0)")
        except subprocess.TimeoutExpired:
            print("[!] Timeout (12s exceeded)")
        except FileNotFoundError:
            print(f"[!] Script missing or non-executable in path: {cmd}")
        except Exception as e:
            print(f"[!] Error: {e}")
        print("-" * 60)

if __name__ == "__main__":
    run_suite()
