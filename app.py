import subprocess
import hashlib

# Insecure: hardcoded password
password = "admin123"

def run_command(cmd):
    # Insecure: shell=True allows command injection
    return subprocess.call(cmd, shell=True)

def hash_password(data):
    # Insecure: MD5 is a weak hashing algorithm
    return hashlib.md5(data.encode()).hexdigest()

def calculate(expression):
    # Insecure: eval runs arbitrary code
    return eval(expression)

if __name__ == "__main__":
    print(hash_password(password))
