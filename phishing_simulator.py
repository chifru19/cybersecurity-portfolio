import sys
import smtplib
from email.message import EmailMessage

def generate_phishing_template(recipient="employee@example.com"):
    print(f"\n[*] Generating phishing simulation template for: {recipient}")
    print("-" * 50)

    msg = EmailMessage()
    msg['Subject'] = "URGENT: Immediate Password Reset Required"
    msg['From'] = "security-admin@corporate-internal-auth.com"
    msg['To'] = recipient

    body = f"""
    Dear Employee,

    We have detected unusual sign-in activity on your corporate account for campaign 'Q3-Security-Awareness'. 
    To protect your account, you are required to verify your credentials within 24 hours.

    Please click the secure link below to verify your identity:
    https://internal-auth-portal-secure-login.com/verify?user={recipient}

    If you did not initiate this request, please contact IT Security immediately.

    Best regards,
    Corporate IT Security Team
    """
    msg.set_content(body.strip())
    return msg

def send_to_mailpit(msg):
    print("[*] Dispatching email to local Mailpit server (localhost:1025)...")
    try:
        with smtplib.SMTP('localhost', 1025) as server:
            server.send_message(msg)
        print("[+] Success! Simulation email sent to Mailpit (Check http://localhost:8025)")
    except Exception as e:
        print(f"[!] Error: Failed to connect to Mailpit. Is it running? Details: {e}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "employee@example.com"
    auto_send = "--send" in sys.argv

    template_msg = generate_phishing_template(target)
    
    print("\n[+] Phishing Template Generated Successfully:")
    print("-" * 50)
    print(template_msg)
    print("-" * 50)

    if auto_send:
        send_to_mailpit(template_msg)
    else:
        print("[*] Note: Run with '--send' flag to push this template directly to your local Mailpit server.")
        print("    Example: python3 phishing_simulator.py employee@example.com --send\n")
