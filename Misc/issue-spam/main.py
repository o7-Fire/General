from github import Github
import time
import string
import random
import base64

def encodebase64(text):
    return base64.b64encode(text.encode('ascii')).decode('ascii')

while True:
    try:
        g = Github("")
        repo = g.get_repo("Nexity/testa")
        
        while True:
            titleran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
            descran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=200))
            repo.create_issue(title=titleran, body=("current time : " + time.ctime()))
            repo.create_file(titleran + ".txt", titleran, encodebase64(descran), branch="main")
            #time.sleep(1)
    except:
        time.sleep(10)
        print("ratelimited")
