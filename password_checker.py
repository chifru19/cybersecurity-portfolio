import requests
import sys
import hashlib

def verify_pwd(val):
    digest = hashlib.sha1(val.encode('utf-8')).hexdigest().upper()
    pfx, sfx = digest[:5], digest[5:]
    endpoint = f'https://api.pwnedpasswords.com/range/{pfx}'
    
    try:
        res = requests.get(endpoint, timeout=5)
        if res.status_code != 200:
            raise RuntimeError(f'API error: {res.status_code}')
            
        for h, count in (line.split(':') for line in res.text.splitlines()):
            if h == sfx:
                print(f"    [CRITICAL] Found in {count} public breaches!")
                return
        print("    [SECURE] Not found in any known public breach databases.")
    except Exception as err:
        print(f"    [ERROR] Check failed: {err}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        verify_pwd(sys.argv[1])
    else:
        print("Usage: python3 password_checker.py <password>")
