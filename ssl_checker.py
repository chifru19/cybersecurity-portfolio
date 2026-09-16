import ssl
import socket
from datetime import datetime
import sys

def check_ssl(hostname="github.com", port=443):
    print(f"\n[*] Inspecting SSL/TLS certificate for: {hostname}:{port}")
    print("-" * 50)
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                print(f"[+] Common Name (CN): {cert.get('subject', ((('commonName',),),))[0][0][1]}")
                print(f"[+] Issuer: {dict(x[0] for x in cert.get('issuer', []))}")
                
                expiry_date = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
                days_remaining = (expiry_date - datetime.now()).days
                
                print(f"[+] Expiration Date: {expiry_date}")
                if days_remaining > 30:
                    print(f"    [SECURE] Certificate is valid for another {days_remaining} days.")
                else:
                    print(f"    [WARNING] Certificate expires soon! Only {days_remaining} days remaining.")
    except Exception as e:
        print(f"[!] Error connecting or retrieving SSL certificate: {e}")
    print("-" * 50)
    print("[+] SSL check completed!\n")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "github.com"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 443
    check_ssl(target, port)
