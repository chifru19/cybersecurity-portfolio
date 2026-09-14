import re
import sys
import os

# Define regex patterns for common sensitive secrets
SECRET_PATTERNS = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "GitHub Personal Access Token": r"ghp_[a-zA-Z0-9]{36}",
    "Generic API Key": r"(?i)(api_key|apikey|secret)['\"]?\s*[:=]\s*['\"]?[a-zA-Z0-9_\-]{16,45}['\"]?",
    "Hardcoded Password": r"(?i)(password|passwd|pwd)['\"]?\s*[:=]\s*['\"]?[^\s'\"]{6,30}['\"]?"
}

def scan_file(filepath):
    print(f"[*] Scanning file for secrets: {filepath}")
    findings = 0
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            for line_num, line in enumerate(f, 1):
                for secret_type, pattern in SECRET_PATTERNS.items():
                    if re.search(pattern, line):
                        print(f"    [ALERT] Found potential {secret_type} on line {line_num}!")
                        findings += 1
    except Exception as e:
        print(f"[!] Could not read file {filepath}: {e}")
    return findings

def scan_directory(directory="."):
    print("\n[*] Starting Automated Secret Scan...\n" + "-"*40)
    total_findings = 0
    
    # Walk through directory, ignoring hidden dirs like .git and venv
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ['.git', 'venv', '__pycache__']]
        for file in files:
            if file.endswith(('.py', '.json', '.env', '.txt', '.yml', '.yaml')):
                filepath = os.path.join(root, file)
                total_findings += scan_file(filepath)
                
    print("-" * 40)
    if total_findings > 0:
        print(f"[!] Scan complete: Found {total_findings} potential secret leak(s)!")
        sys.exit(1)
    else:
        print("[+] Scan complete: No secrets found. Code looks clean!")

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    scan_directory(target_dir)
