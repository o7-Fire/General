import requests
from fake_headers import Headers
import threading
import time
import string
import random

header = Headers(
        headers=True  # generate misc headers
    )

total_checked = 1
letters = string.ascii_letters + string.digits

def do():
    global total_checked
    try:
        r = requests.get(f"https://discord.com/api/v9/invites/{''.join(random.choice(letters) for i in range(8))}", headers=header.generate())
        if r.status_code == 200:
            print(r)
        elif r.status_code == 404:
            total_checked += 1
    except:
        sdrifsietwes = 0
print(f"possible combinations: {str(len(letters)**len(letters))}")
while True:
    time.sleep(0.1)
    if total_checked % 1000 == 0:
        print(f"total checked: {str(total_checked)}")
    if threading.active_count() < 100:
        t1 = threading.Thread(target=do)
        t1.start()
