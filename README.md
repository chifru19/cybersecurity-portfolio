# Cybersecurity & DevSecOps Engineering Portfolio

Welcome to my professional cybersecurity engineering and automation portfolio! This repository contains 10 production-grade Python tools designed to automate security tasks, audit vulnerabilities, implement cryptography, and enforce DevSecOps best practices across both local environments and live production assets like **frankfru.com**.

---

## 📊 Interactive Command Center & Dashboard

You can launch the interactive Streamlit command center locally:
```bash
streamlit run app.py
```
* **Live Execution Sandbox:** Features a built-in UI terminal executor allowing real-time tool triggering against target endpoints directly from the browser interface.

---

## 🛠️ Project Inventory (10/10 Completed)

| Project ID | Script Name | Description |
| :--- | :--- | :--- |
| **Project 1** | `scanner.py` | Web Application Vulnerability Scanner (Headers & Exposed Files) |
| **Project 2** | `log_analyzer.py` | Log Analysis & Threat Detection (Brute-Force & Reconnaissance) |
| **Project 3** | `file_encryptor.py` | Encrypted File Share & Secure Uploader (Fernet Symmetric Encryption) |
| **Project 4** | `secret_scanner.py` | Automated Git Repository Secret Scanner (Regex Credential Leak Detector) |
| **Project 5** | `port_scanner.py` | Network Port Scanner (Multi-threaded TCP Socket Mapper) |
| **Project 6** | `phishing_simulator.py` | Phishing Awareness Simulation Tool (Educational Corporate Templates) |
| **Project 7** | `jwt_auditor.py` | JWT Security Auditor (Misconfiguration & Signature Bypass Checker) |
| **Project 8** | `ssl_checker.py` | SSL/TLS Certificate Expiration & Security Inspector |
| **Project 9** | `password_checker.py` | Password Strength & Breach Checker (HIBP k-Anonymity API Integration) |
| **Project 10** | `portfolio_dashboard.py` | Master Portfolio Summary & Health Dashboard (CLI & Streamlit Web App) |

---

## 🚀 Live Production Integration & Dogfooding (`frankfru.com`)

Rather than operating in isolation, this toolchain is actively dogfooded against **frankfru.com**:
* **Perimeter Audits:** Regular header hardening reviews (Content Security Policy, HSTS, X-Frame-Options) and transport reconnaissance.
* **PKI Tracking:** Monitoring live TLS certificate expiration health to prevent unexpected downtime.
* **Edge Mapping:** Verifying public Cloudflare edge ports (`80/443`).

---

## ⚙️ DevSecOps & CI/CD Pipelines

This repository implements automated continuous integration using GitHub Actions across two core workflows:
1. **Repository Health CI (`security_ci.yml`):** Runs on every push or pull request to the `main` branch, provisioning an isolated Ubuntu environment running Python 3.12 to ensure 100% dependency compatibility and script execution integrity.
2. **Production Watchdog (`prod-monitor.yml`):** Scheduled daily automation running security checks and telemetry against **frankfru.com**.

---

## 👤 Author & Contact

* **Name:** Frank Fru
* **Website:** [frankfru.com](https://frankfru.com)
* **GitHub:** [chifru19](https://github.com/chifru19)
* **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/chifru19)
* **Email:** chifru19@googlemail.com
