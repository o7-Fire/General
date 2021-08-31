import os
import threading

tokens = [

]

def startbot(token):
	os.system("python main.py " + token)
for token in tokens:
	
	t = threading.Thread(target=startbot, args=(token,))
	t.start()
