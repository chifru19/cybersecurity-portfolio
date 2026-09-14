import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

def generate_phishing_template(target_email, campaign_name):
    print(f"[*] Generating phishing simulation template for: {target_email}")
    
    msg = MIMEMultipart()
    msg['Subject'] = "URGENT: Immediate Password Reset Required"
    msg['From'] = "security-admin@corporate-internal-auth.com"
    msg['To'] = target_email

    body = f"""
    Dear Employee,

    We have detected unusual sign-in activity on your corporate account for campaign '{campaign_name}'. 
    To protect your account, you are required to verify your credentials within 24 hours.

    Please click the secure link below to verify your identity:
    https://internal-auth-portal-secure-login.com/verify?user={target_email}

    If you did not initiate this request, please contact IT Security immediately.

    Best regards,
    Corporate IT Security Team
    """

    msg.attach(MIMEText(body, 'plain'))
    
    print("\n[+] Phishing Template Generated Successfully:")
    print("-" * 50)
    print(msg.as_string())
    print("-" * 50)
    print("[*] Note: To send this via local SMTP server (like Mailpit/Postfix), configure your relay host.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "employee@example.com"
    campaign = sys.argv[2] if len(sys.argv) > 2 else "Q3-Security-Awareness"
    generate_phishing_template(target, campaign)
