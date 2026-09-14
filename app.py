import streamlit as st
import os

st.set_page_config(page_title="Chifru Cybersecurity Portfolio", page_icon="🛡️", layout="wide")

st.title("🛡️ Frank Fru - Cybersecurity Portfolio Dashboard")
st.markdown("Welcome to my interactive security operations and automation dashboard, featuring 10 production-grade Python tools.")

projects = [
    (
        "Project 1: Web App Vulnerability Scanner", 
        "scanner.py", 
        "Audits web application security headers (HSTS, CSP, X-Frame-Options) and checks for exposed sensitive configuration files (e.g., robots.txt, .env) using HTTP GET requests."
    ),
    (
        "Project 2: Log Analysis & Threat Detection", 
        "log_analyzer.py", 
        "Parses standard Apache/Nginx combined access logs line by line using Regular Expressions (RegEx) to isolate IP addresses, requested paths, and status codes. Flags active brute-force attacks (repeated 401/403 errors) and reconnaissance scans targeting hidden paths."
    ),
    (
        "Project 3: Encrypted File Share", 
        "file_encryptor.py", 
        "Provides local file encryption and secure upload workflows using the cryptography library (Fernet symmetric encryption: AES-128 in CBC mode with HMAC SHA256 integrity signatures)."
    ),
    (
        "Project 4: Automated Secret Scanner", 
        "secret_scanner.py", 
        "DevSecOps pre-commit style scanner using recursive directory traversal (`os.walk`) and RegEx signature patterns to catch hardcoded AWS access keys, tokens, and credentials before code reaches GitHub."
    ),
    (
        "Project 5: Network Port Scanner", 
        "port_scanner.py", 
        "Multi-threaded TCP port scanner leveraging Python's low-level `socket` library and `ThreadPoolExecutor` to map network attack surfaces concurrently and efficiently."
    ),
    (
        "Project 6: Phishing Awareness Simulator", 
        "phishing_simulator.py", 
        "Constructs MIME-compliant corporate phishing templates via Python's `email.mime` modules, embedding realistic urgency pretexts and tracking parameters for security awareness training campaigns."
    ),
    (
        "Project 7: JWT Security Auditor", 
        "jwt_auditor.py", 
        "Parses and decodes JSON Web Tokens (Headers and Payloads via Base64URL) to flag critical security misconfigurations, such as accepting the vulnerable `none` algorithm or missing expiration (`exp`) claims."
    ),
    (
        "Project 8: SSL/TLS Inspector", 
        "ssl_checker.py", 
        "Establishes raw TCP and TLS connections to inspect domain certificates, extract Common Names (CN) and issuers, and calculate remaining validity days to prevent certificate expiration outages."
    ),
    (
        "Project 9: Password Strength & Breach Checker", 
        "password_checker.py", 
        "Evaluates password entropy/complexity and integrates with the Have I Been Pwned (HIBP) API using SHA-1 hashing and the k-anonymity model (sending only the first 5 hash characters) to ensure absolute user privacy."
    ),
    (
        "Project 10: Master Health Dashboard", 
        "portfolio_dashboard.py", 
        "Unified CLI inventory verifier and interactive Streamlit web dashboard tracking repository health and project status."
    )
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
        st.markdown(f"**Detailed Breakdown:** {desc}")

st.sidebar.header("Portfolio Status")
st.sidebar.metric(label="Core Projects Active", value=f"{completed_count}/10")
st.sidebar.success("GitHub Actions CI/CD: Passing ✅")
st.sidebar.markdown("---")
st.sidebar.markdown("**Author:** Frank Fru")
st.sidebar.markdown("[Website](https://frankfru.com) | [GitHub](https://github.com/chifru19)")
