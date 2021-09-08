#generates new screenshots
import requests
import string
import random
import time
import os

S = 6
while True:
  finalmessage = ""
  for i in range(5):
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = S))
    finalmessage = finalmessage + f"https://prnt.sc/1{ran}\n" #7 digit only started with 1
  requests.post(os.getenv("webhook"), {"content":finalmessage})
  time.sleep(1)
