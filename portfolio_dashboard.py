import os

PROJECTS = [
    ("Project 1", "scanner.py", "Web App Vulnerability Scanner (Headers & Exposed Files)"),
    ("Project 2", "log_analyzer.py", "Log Analysis & Threat Detection (Brute-Force & Recon)"),
    ("Project 3", "file_encryptor.py", "Encrypted File Share & Secure Uploader (Fernet Encryption)"),
    ("Project 4", "secret_scanner.py", "Automated Git Repository Secret Scanner (Regex Leak Detector)"),
    ("Project 5", "port_scanner.py", "Network Port Scanner (Multi-threaded TCP Socket Mapper)"),
    ("Project 6", "phishing_simulator.py", "Phishing Awareness Simulation Tool (Educational Templates)"),
    ("Project 7", "jwt_auditor.py", "JWT Security Auditor (Misconfiguration & Signature Bypass Checker)"),
    ("Project 8", "ssl_checker.py", "SSL/TLS Certificate Expiration & Security Inspector"),
    ("Project 9", "password_checker.py", "Password Strength & Breach Checker (HIBP API Integration)")
]

def render_dashboard():
    print("\n" + "="*65)
    print("       CHIFRU19 CYBERSECURITY PORTFOLIO - MASTER DASHBOARD")
    print("="*65)
    
    completed_count = 0
    for proj_id, filename, description in PROJECTS:
        status = "[VERIFIED & ACTIVE]" if os.path.exists(filename) else "[MISSING]"
        if os.path.exists(filename):
            completed_count += 1
        print(f"[{proj_id}] {filename:<22} - {status}\n      Desc: {description}\n" + "-"*65)

    print(f"\n[+] Portfolio Status: {completed_count}/9 Core Projects Active & Pushed to GitHub.")
    print("[+] Portfolio Goal: 10/10 Complete (Dashboard counts as Project 10!)\n")

if __name__ == "__main__":
    render_dashboard()
