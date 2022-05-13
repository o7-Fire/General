import requests
import os
import random
import string
import time
import sys

members = ""
with open("members.txt", "r") as f:
  members = f.read().split("\n")
  
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

#os.system("pip3 install discord.py-self")
try:
  import discord
  from discord import Webhook, AsyncWebhookAdapter
except:
  print("something wrong, send help")

TOKEN = sys.argv[1]
BOTNUM = sys.argv[2]
client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
  if message.author.id == client.user.id and message.content == "a":
    await message.delete()
  if message.content == "ERAUWYVEYWUGVYUWBH":
    channel = client.get_channel(794949269126643713)
    message2 = await channel.fetch_message(794952523496554516)
    emoji = client.get_emoji(830070201654837249)
    await message2.add_reaction('🏴‍☠️')
  if message.content.startswith("AFIDNSIUHGSIHU"):
    invite = message.content.split(" ")[1]
    thenum = message.content.split(" ")[2]
    if thenum == BOTNUM:
      requests.post("https://discordapp.com/api/v6/invites/" + invite,headers={'authorization':TOKEN})
  if message.content == "bETBIUTWUNINTJ":
    if message.author.id == client.user.id:
      await message.delete()
    while True:
      time.sleep(1.2)
      print("ok")
      #await message.channel.send("<@854577311810060288>")

      #finalmessage = f""
      #for i in range(60):
      #  finalmessage = finalmessage + f"<@{random.choice(members)}> "
      #await message.channel.send(finalmessage) 
      
      #await message.channel.send(finalmessage + "https://cdn.discordapp.com/attachments/909737041913327656/910888181874978846/jesus_sermon_mount.jpeg\nhttps://cdn.discordapp.com/attachments/909737041913327656/910909673975201842/santajesus1.jpg\nhttps://cdn.discordapp.com/attachments/909737041913327656/910909727272214598/21readers-jesus3-articleLarge.jpg")

#try:
client.run(TOKEN)
#except:
#  print("token incorrect: " + TOKEN)
