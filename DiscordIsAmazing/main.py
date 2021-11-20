import requests
import os
import random
import string
import time

members = ""
with open("members.txt", "r") as f:
  members = f.read().split("\n")
  
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

os.system("pip3 install discord.py-self")
try:
  import discord
  from discord import Webhook, AsyncWebhookAdapter
except:
  print("something wrong, send help")

TOKEN = os.getenv("TOKEN1")
client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
  if message.author.id == client.user.id and message.content == "a":
    await message.delete()
  if message.content == "bETBIUTWUNINTJ":
    #await message.delete()
    while True:
      time.sleep(1.2)
      print("ok")
      finalmessage = f""
      for i in range(60):
        finalmessage = finalmessage + f"<@{random.choice(members)}> "
      await message.channel.send(finalmessage) #"https://cdn.discordapp.com/attachments/909737041913327656/910888181874978846/jesus_sermon_mount.jpeg\nhttps://cdn.discordapp.com/attachments/909737041913327656/910909673975201842/santajesus1.jpg\nhttps://cdn.discordapp.com/attachments/909737041913327656/910909727272214598/21readers-jesus3-articleLarge.jpg")

client.run(TOKEN)
