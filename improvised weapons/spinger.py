import os
import random
import string
import time

os.system("pip3 install discord.py-self")
try:
  import discord
  from discord import Webhook, AsyncWebhookAdapter
except:
  print("something wrong, send help")

TOKEN = ""
client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
  if message.author.id == client.user.id and message.content == "a":
    await message.delete()
  if message.author.id == client.user.id and message.content == "b":
    await message.delete()
    while True:
      time.sleep(1.1)
      for guild in client.guilds:
        if guild.id == 737716105812115617:
          for channel in guild.text_channels:
            if channel.id == 777562915917791252:
              loop = 0
              finalmessage = f""
              for member in guild.members:
                if loop != 50: #how much you wanna ping each message
                  finalmessage = finalmessage + f"<@{member.id}> "
                  loop = loop + 1
              await channel.send(finalmessage)

client.run(TOKEN)
