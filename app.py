import subprocess
import hashlib
import os

password = os.environ.get("APP_PASSWORD", "")

def run_command(cmd_list):
    return subprocess.call(cmd_list, shell=False)

def hash_password(data):
    return hashlib.sha256(data.encode()).hexdigest()

def calculate(expression):
    return int(expression)

if __name__ == "__main__":
    print(hash_password(password))
