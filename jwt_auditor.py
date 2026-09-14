import json
import base64
import sys

def decode_base64_url(input_str):
    # Fix padding for base64 decoding
    padding = '=' * (4 - (len(input_str) % 4))
    return base64.urlsafe_b64decode(input_str + padding).decode('utf-8')

def audit_jwt(token):
    print("\n[*] Auditing JWT for security misconfigurations...\n" + "-"*50)
    try:
        parts = token.split('.')
        if len(parts) != 3:
            print("[!] Error: Invalid JWT format. A valid token must have 3 parts separated by dots.")
            return

        header_json = json.loads(decode_base64_url(parts[0]))
        payload_json = json.loads(decode_base64_url(parts[1]))

        print(f"[+] Decoded Header: {json.dumps(header_json, indent=2)}")
        print(f"[+] Decoded Payload: {json.dumps(payload_json, indent=2)}")

        print("\n[+] Security Analysis:")
        alg = header_json.get("alg", "").upper()
        
        # Check 1: 'none' algorithm vulnerability
        if alg == "NONE":
            print("    [CRITICAL] Token uses the 'none' algorithm! This allows signature bypass.")
        else:
            print(f"    [SECURE] Algorithm used: {alg}")

        # Check 2: Weak HMAC or missing expiration
        if "exp" not in payload_json:
            print("    [WARNING] Missing 'exp' (Expiration) claim. Token never expires.")
        else:
            print("    [SECURE] Expiration claim ('exp') is present.")

    except Exception as e:
        print(f"[!] Failed to parse JWT: {e}")
    print("-" * 50 + "\n[+] JWT audit completed!\n")

if __name__ == "__main__":
    # Example mock token for testing
    sample_token = "eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9."
    token_to_audit = sys.argv[1] if len(sys.argv) > 1 else sample_token
    audit_jwt(token_to_audit)
