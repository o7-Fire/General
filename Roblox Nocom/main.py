import keep_alive
keep_alive.keep_alive()
import os
import random
import time
import discord
import threading
import requests

headers = {
  #"authority":"www.roblox.com",
  #"scheme":"https",
  #"path":"/games/getgameinstancesjson?placeId=166986752&startindex=0",
  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
  "accept-language": "en-US,en;q=0.9",
  "cache-control": "max-age=0",
  "sec-ch-ua": "\"Chromium\";v=\"94\", \"Google Chrome\";v=\"94\", \";Not A Brand\";v=\"99\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\"",
  "sec-fetch-dest": "document",
  "sec-fetch-mode": "navigate",
  "sec-fetch-site": "none",
  "sec-fetch-user": "?1",
  "upgrade-insecure-requests": "1",
  "cookie": os.getenv("COOKIE")
}

TOKEN = os.getenv("TOKEN")
client = discord.Client()
whitelisted = [854577311810060288]

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')
  
@client.event
async def on_message(message):
  if message.content == "active":
    await message.channel.send("yes")
  if (message.author.id in whitelisted) == False:
    return
  if message.content.startswith("getservers"):
    if message.content == "getservers":
      await message.channel.send("usage: getservers [placeId]")
    else:
      id = message.content.replace("getservers ", "")
      api = f"https://www.roblox.com/games/getgameinstancesjson?placeId={id}&startindex=0"
      starttime = time.time()
      r = requests.get(api, headers=headers).json()
      await message.channel.send(f"total servers: {r['TotalCollectionSize']}\ntime taken: {time.time() - starttime}s")

  if message.content.startswith("getserver"):
    if message.content == "getserver":
      await message.channel.send("usage: getserver [placeId] [serverNumber]")
    else:
      id = message.content.split(" ")[1]
      num = message.content.split(" ")[2]
      api = f"https://www.roblox.com/games/getgameinstancesjson?placeId={id}&startindex={num}"
      r = requests.get(api, headers=headers).json()
      
      finalmessage = ""
      loop = 0
      for server in r["Collection"]:
        loop += 1
        s = server
        finalmessage += f"Server {loop}: Ping {s['Ping']}, Players {s['PlayersCapacity']}, Slow Server {s['ShowSlowGameMessage']}, GUID {s['Guid']}\n"
      await message.channel.send(f"```{finalmessage}```")


    
client.run(TOKEN)
