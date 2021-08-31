import discord
import sys
import time
import requests
import random

if len(sys.argv) == 2:
    token = sys.argv[1]
    whitelisted = [854577311810060288]
    client = discord.Client()
    
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        
    @client.event
    async def on_message(message):
        if message.author.id in whitelisted:
            if "testb " in message.content:
                msgs = message.content.split("testb ")[1]
                await message.channel.send(msgs)
            if "testc " in message.content:
                msgs = message.content.split("testc ")[1]
                while True:
                    await message.channel.send(msgs)
                    time.sleep(1)
            if "testd " in message.content:
                theinvite = message.content.split("testd ")[1]
                time.sleep(random.randint(6, 12)) #dumbass
                r = requests.post("https://discordapp.com/api/v6/invites/" + theinvite, headers={'authorization': token})
                time.sleep(random.randint(6, 12))
                await message.channel.send("joined: " + r.text.split('id": "')[1].split('", "name')[0])
    
    client.run(token)
else:
    print("usage: python main.py [token]")
