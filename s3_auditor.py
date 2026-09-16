import sys
import requests

def audit_bucket(bucket_name):
    print(f"\n[*] Auditing Storage Bucket: {bucket_name}")
    print("-" * 50)
    
    # Standard AWS S3 public endpoint check
    url = f"https://{bucket_name}.s3.amazonaws.com"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"    [CRITICAL] Bucket '{bucket_name}' is publicly readable (Listing enabled)!")
        elif response.status_code == 403:
            print(f"    [SECURE] Bucket '{bucket_name}' access is properly denied/restricted (403 Forbidden).")
        elif response.status_code == 404:
            print(f"    [INFO] Bucket '{bucket_name}' does not exist or is private.")
        else:
            print(f"    [INFO] Received status code {response.status_code} for bucket.")
    except Exception as e:
        print(f"    [ERROR] Audit connection failed: {e}")
        
    print("-" * 50 + "\n[+] Cloud storage audit completed!\n")

if __name__ == "__main__":
    b_name = sys.argv[1] if len(sys.argv) > 1 else "test-bucket-example"
    audit_bucket(b_name)
