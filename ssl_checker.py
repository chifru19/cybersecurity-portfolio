import socket
import ssl
import sys
from datetime import datetime, timezone

def check_ssl_certificate(hostname, port=443):
    print(f"\n[*] Inspecting SSL/TLS certificate for: {hostname}:{port}\n" + "-"*50)
    
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
                # Extract certificate details
                subject = dict(x[0] for x in cert.get('subject', []))
                issuer = dict(x[0] for x in cert.get('issuer', []))
                not_after_str = cert.get('notAfter')
                
                print(f"[+] Common Name (CN): {subject.get('commonName', 'N/A')}")
                print(f"[+] Issuer: {issuer.get('commonName', 'N/A')}")
                
                # Parse expiration date
                expiry_date = datetime.strptime(not_after_str, '%b %d %H:%M:%S %Y %Z')
                days_remaining = (expiry_date - datetime.now(datetime.timezone.utc)).days
                
                print(f"[+] Expiration Date: {expiry_date}")
                
                if days_remaining < 30:
                    print(f"    [WARNING] Certificate expires soon! Only {days_remaining} days remaining.")
                else:
                    print(f"    [SECURE] Certificate is valid for another {days_remaining} days.")
                    
    except Exception as e:
        print(f"[!] Error connecting or retrieving SSL certificate: {e}")
        
    print("-" * 50 + "\n[+] SSL check completed!\n")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "github.com"
    check_ssl_certificate(target)
