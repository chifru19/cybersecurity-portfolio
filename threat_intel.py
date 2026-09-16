import sys
import requests
import json

def check_ip(ip_address):
    print(f"\n[*] Querying Threat Intelligence for IP: {ip_address}")
    print("-" * 50)
    
    # Using a public IP geolocation/reputation lookup endpoint as an educational baseline
    url = f"http://ip-api.com/json/{ip_address}"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'success':
                print(f"    [INFO] Country: {data.get('country')} ({data.get('countryCode')})")
                print(f"    [INFO] Region/City: {data.get('regionName')}, {data.get('city')}")
                print(f"    [INFO] ISP / Org: {data.get('isp')} / {data.get('org')}")
                print(f"    [SECURE] IP record retrieved successfully from registry.")
            else:
                print(f"    [WARNING] IP lookup returned failure status: {data.get('message', 'Unknown')}")
        else:
            print(f"    [ERROR] API request failed with status code {response.status_code}")
    except Exception as e:
        print(f"    [ERROR] Connection failed: {e}")
        
    print("-" * 50 + "\n[+] Threat Intelligence lookup completed!\n")

if __name__ == "__main__":
    target_ip = sys.argv[1] if len(sys.argv) > 1 else "8.8.8.8"
    check_ip(target_ip)
