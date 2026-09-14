from cryptography.fernet import Fernet
import sys
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as k: k.write(key)
    print("[+] Key generated")

def encrypt_file(filename):
    if not os.path.exists("secret.key"): generate_key()
    f = Fernet(open("secret.key", "rb").read())
    with open(filename, "rb") as file: data = file.read()
    with open(filename + ".enc", "wb") as file: file.write(f.encrypt(data))
    print(f"[+] Encrypted: {filename}.enc")

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "encrypt": encrypt_file(sys.argv[2])
