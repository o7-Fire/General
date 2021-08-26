
import keep_alive
keep_alive.keep_alive()
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

TOKEN = os.getenv("TOKEN")
client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
  if message.author.id == client.user.id and message.content == "abcdetest":
    while True:
      await message.channel.send("pls hunt")
      time.sleep(random.randint(2, 4))
      await message.channel.send("pls fish")
      time.sleep(random.randint(2, 4))
      await message.channel.send("pls beg")
      time.sleep(random.randint(2, 4))
      await message.channel.send("pls dig")
      time.sleep(random.randint(35, 40))

client.run(TOKEN)
