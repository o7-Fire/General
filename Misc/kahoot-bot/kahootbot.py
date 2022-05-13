from kahoot import client
import threading

pin = 280038 #the kahoot's pin
name = "nexity" #name here

def create_bot(i):
    bot = client()
    gay = name + str(i)
    bot.join(pin, gay)
    def joinHandle():
        pass
    bot.on("joined",joinHandle)
    
for i in range(1000): #change amount to how many bots you want
    t = threading.Thread(target=create_bot, args=(i,))
    t.start()
