import time
import os
import threading


for i in range(5):
    def p():
        os.system('node main.js NBot' + str(i+1))
        #command1 = subprocess.Popen(['node', 'main.js', 'NBot' + str(i+1)])
    t = threading.Thread(target=p)
    t.start()
    time.sleep(6)
