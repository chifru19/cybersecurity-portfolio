import socket
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def scan_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"    [OPEN] Port {port} is open")
        s.close()
    except Exception:
        pass

def scan_target(target_host, ports_to_scan=range(1, 1024)):
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"[!] Hostname could not be resolved: {target_host}")
        return

    print("\n" + "="*50)
    print(f"[*] Starting Port Scan on target: {target_ip}")
    print(f"[*] Time started: {str(datetime.now())}")
    print("="*50 + "\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports_to_scan:
            executor.submit(scan_port, target_ip, port)

    print("\n" + "="*50)
    print("[+] Port scanning completed!")
    print("="*50 + "\n")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    scan_target(target)
