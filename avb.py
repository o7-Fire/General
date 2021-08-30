# for artic vault
import keep_alive
keep_alive.keep_alive()
import os
import random
import string
import time
import requests

os.system("pip3 install discord.py-self")
try:
  import discord
  from discord import Webhook, AsyncWebhookAdapter
  import aiohttp
except:
  print("something wrong, send help")

TOKEN = os.getenv("TOKEN")
client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
  if message.content == "getinvite" and message.channel.id == 840041811384860709:
    async with aiohttp.ClientSession() as session:
      webhook = Webhook.from_url('webhook_url', adapter=AsyncWebhookAdapter(session))
      r = requests.get("https://raw.githubusercontent.com/o7-Fire/General/master/idb.txt").text.split("\n")
      totalcount = 0
      totalmessage = ""
      for lines in r:
        if totalcount % 5 == 0 and (len(r) - totalcount) >= 5:
          totalmessage = totalmessage + lines + "\n"
        else:
          await webhook.send(totalmessage)
          totalmessage = ""
        
client.run(TOKEN)
