import requests
import string
import random
import time
import os

S = 6
while True:
  ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = S))
  requests.post(os.getenv("webhook"), {"content":f"https://prnt.sc/{ran}"})
  time.sleep(3)
