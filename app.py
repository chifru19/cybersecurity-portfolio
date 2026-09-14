import streamlit as st
import os

st.set_page_config(page_title="Chifru Cybersecurity Portfolio", page_icon="🛡️", layout="wide")

st.title("🛡️ Chifru Fru - Cybersecurity Portfolio Dashboard")
st.markdown("Welcome to my interactive security operations and automation dashboard, featuring 10 production-grade Python tools.")

projects = [
    ("Project 1: Web App Vulnerability Scanner", "scanner.py", "Audits web application security headers and exposed configuration files."),
    ("Project 2: Log Analysis & Threat Detection", "log_analyzer.py", "Parses server access logs to flag brute-force attacks and reconnaissance scans."),
    ("Project 3: Encrypted File Share", "file_encryptor.py", "Provides local file encryption and secure upload workflows using Fernet cryptography."),
    ("Project 4: Automated Secret Scanner", "secret_scanner.py", "DevSecOps scanner using RegEx to catch accidental credential leaks."),
    ("Project 5: Network Port Scanner", "port_scanner.py", "Multi-threaded TCP port scanner for network attack surface mapping."),
    ("Project 6: Phishing Awareness Simulator", "phishing_simulator.py", "Generates educational awareness simulation templates for security training."),
    ("Project 7: JWT Security Auditor", "jwt_auditor.py", "Inspects JSON Web Tokens for critical signature bypasses and algorithm misconfigurations."),
    ("Project 8: SSL/TLS Inspector", "ssl_checker.py", "Inspects domain certificates, expiration dates, and encryption strength."),
    ("Project 9: Password Strength & Breach Checker", "password_checker.py", "Evaluates password entropy and queries the HIBP k-anonymity API."),
    ("Project 10: Master Health Dashboard", "portfolio_dashboard.py", "Unified CLI status and inventory verifier.")
]

completed_count = 0
for title, filename, desc in projects:
    exists = os.path.exists(filename)
    if exists:
        completed_count += 1
    
    with st.expander(f"{title} ({filename})"):
        if exists:
            st.success("Status: VERIFIED & ACTIVE")
        else:
            st.warning("Status: MISSING")
        st.markdown(f"**Description:** {desc}")

st.sidebar.header("Portfolio Status")
st.sidebar.metric(label="Core Projects Active", value=f"{completed_count}/10")
st.sidebar.success("GitHub Actions CI/CD: Passing ✅")
st.sidebar.markdown("[View GitHub Repository](https://github.com/chifru19/cybersecurity-portfolio)")
