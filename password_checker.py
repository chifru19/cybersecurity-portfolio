import requests
import hashlib
import sys

def check_password_pwned(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, tail = sha1password[:5], sha1password[5:]
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            raise RuntimeError(f'Error fetching data: {response.status_code}')
            
        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == tail:
                return int(count)
        return 0
    except Exception as e:
        print(f"[!] Could not check breach database: {e}")
        return None

def evaluate_password(password):
    print(f"\n[*] Evaluating password security...\n" + "-"*50)
    
    # Basic complexity checks
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    print(f"[+] Password Length: {length} characters")
    
    if length >= 12 and has_upper and has_lower and has_digit and has_symbol:
        print("    [SECURE] Strong complexity criteria met.")
    else:
        print("    [WARNING] Weak complexity. Recommended: 12+ chars with upper, lower, numbers, and symbols.")

    # Breach check
    count = check_password_pwned(password)
    if count is not None:
        if count > 0:
            print(f"    [CRITICAL] Password has been found in {count} public data breaches! Do not use this.")
        else:
            print("    [SECURE] Good news! Password was not found in any known public breach databases.")
            
    print("-" * 50 + "\n[+] Password evaluation completed!\n")

if __name__ == "__main__":
    target_pwd = sys.argv[1] if len(sys.argv) > 1 else "Password123!"
    evaluate_password(target_pwd)
