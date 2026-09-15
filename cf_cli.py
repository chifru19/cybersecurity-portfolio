import argparse
import sys
import requests

API_BASE = "https://api.cloudflare.com/client/v4"
CLOUDFLARE_API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")

def get_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

def deploy_rules(token, zone_ids):
    phase = "http_request_firewall_custom"
    rule_payload = {
        "name": "Block Sensitive Files",
        "description": "CLI automated block for sensitive configuration assets",
        "expression": '(http.request.uri.path contains ".git" or http.request.uri.path contains ".env" or http.request.uri.path contains "config.json" or http.request.uri.path contains "backup.zip")',
        "action": "block",
        "enabled": True
    }

    for zone_id in zone_ids:
        print(f"[*] Processing Zone ID: {zone_id}")
        ep_url = f"{API_BASE}/zones/{zone_id}/rulesets/phases/{phase}/entrypoint"
        resp = requests.get(ep_url, headers=get_headers(token))

        if resp.status_code == 200:
            ruleset_id = resp.json().get("result", {}).get("id")
            rule_url = f"{API_BASE}/zones/{zone_id}/rulesets/{ruleset_id}/rules"
            add_resp = requests.post(rule_url, headers=get_headers(token), json=rule_payload)

            if add_resp.status_code in [200, 201]:
                print(f"    [+] Successfully deployed block rule to {zone_id}")
            else:
                print(f"    [-] Error deploying to {zone_id}: {add_resp.text}")
        else:
            print(f"    [-] Could not fetch ruleset for {zone_id}: {resp.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cloudflare Security Hardening CLI")
    parser.add_argument("--token", default=DEFAULT_TOKEN, help="Cloudflare API Token")
    parser.add_argument("--zones", required=True, nargs="+", help="Space-separated list of Cloudflare Zone IDs")

    args = parser.parse_args()
    deploy_rules(args.token, args.zones)
