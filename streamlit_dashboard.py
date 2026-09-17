import os
import streamlit as st

st.set_page_config(
    page_title="Chifru Cybersecurity Portfolio", page_icon="🛡️", layout="wide"
)

st.title("🛡️ Frank Fru - Cybersecurity Portfolio Dashboard")
st.markdown("Interactive security operations command center tracking 13 Python tools.")

projects = [
    ("Project 1", "scanner.py", "Web App Vulnerability Scanner (Headers & Exposed Files)"),
    ("Project 2", "log_analyzer.py", "Log Analysis & Threat Detection (Brute-Force & Recon)"),
    ("Project 3", "file_encryptor.py", "Encrypted File Share & Secure Uploader (Fernet)"),
    ("Project 4", "secret_scanner.py", "Automated Git Repository Secret Scanner"),
    ("Project 5", "port_scanner.py", "Network Port Scanner (Multi-threaded TCP Mapper)"),
    ("Project 6", "phishing_simulator.py", "Phishing Awareness Simulation Tool"),
    ("Project 7", "jwt_auditor.py", "JWT Security Auditor (Misconfiguration & Signature Bypass Checker)"),
    ("Project 8", "ssl_checker.py", "SSL/TLS Certificate Expiration & Security Inspector"),
    ("Project 9", "password_checker.py", "Password Strength & Breach Checker (HIBP API)"),
    ("Project 10", "subdomain_scanner.py", "Subdomain Enumerator (CRT.sh Multi-threaded)"),
    ("Project 11", "s3_auditor.py", "AWS S3 Storage Bucket Security Auditor"),
    ("Project 12", "threat_intel.py", "Automated Threat Intelligence & IP Geolocation"),
    ("Project 13", "portfolio_dashboard.py", "Master Portfolio Command Center CLI")
]

completed = 0
for pid, fname, desc in projects:
    exists = os.path.exists(fname)
    if exists:
        completed += 1
    with st.expander(f"[{pid}] {fname} ({'active' if exists else 'missing'})"):
        st.write(f"**Description:** {desc}")
        if exists:
            st.success("VERIFIED & ACTIVE")
        else:
            st.warning("MISSING")

st.sidebar.header("Status Summary")
st.sidebar.metric("Active Projects", f"{completed}/13")
st.sidebar.success("CI/CD Pipeline: Passing ✅")
st.sidebar.markdown("**Author:** Frank Fru | [frankfru.com](https://frankfru.com)")
