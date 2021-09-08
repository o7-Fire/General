#generates new screenshots, set S to 6 for old screenshots
import requests
import string
import random
import time
import os

S = 7
while True:
  finalmessage = ""
  for i in range(5):
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = S))
    finalmessage = finalmessage + f"https://prnt.sc/{ran}\n"
  requests.post(os.getenv("webhook"), {"content":finalmessage})
  time.sleep(1)
