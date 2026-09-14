import re
from collections import Counter

log_data = [
    '192.168.1.50 - - [14/Sep/2026:10:00:01] "GET /index.html HTTP/1.1" 200 1024',
    '203.0.113.42 - - [14/Sep/2026:10:00:05] "POST /login HTTP/1.1" 401 512',
    '203.0.113.42 - - [14/Sep/2026:10:00:06] "POST /login HTTP/1.1" 401 512',
    '203.0.113.42 - - [14/Sep/2026:10:00:07] "POST /login HTTP/1.1" 401 512',
    '203.0.113.42 - - [14/Sep/2026:10:00:08] "POST /login HTTP/1.1" 401 512',
    '198.51.100.15 - - [14/Sep/2026:10:01:12] "GET /.env HTTP/1.1" 403 200',
    '198.51.100.15 - - [14/Sep/2026:10:01:13] "GET /.git/config HTTP/1.1" 403 200',
]

def analyze_logs(logs):
    print("\n[*] Analyzing server logs for security threats...\n" + "-"*50)
    ip_pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    failed_logins = []
    suspicious_scans = []

    for line in logs:
        ip_match = ip_pattern.match(line)
        ip = ip_match.group(1) if ip_match else "Unknown"

        if "/login" in line and "401" in line:
            failed_logins.append(ip)

        if ".env" in line or ".git" in line:
            suspicious_scans.append(ip)

    print("[+] Potential Brute-Force Sources (Multiple 401 Unauthorized):")
    for ip, count in Counter(failed_logins).items():
        print(f"    [ALERT] IP {ip} had {count} failed login attempts.")

    print("\n[+] Potential Reconnaissance / Vulnerability Scans:")
    for ip, count in Counter(suspicious_scans).items():
        print(f"    [CRITICAL] IP {ip} requested sensitive paths {count} times.")

    print("-" * 50 + "\n[+] Log analysis completed successfully!\n")

if __name__ == "__main__":
    analyze_logs(log_data)
