import threading

def spam():
 while True:
  print("hello")

while True:
 t = threading.Thread(target=spam)
 t.start()
