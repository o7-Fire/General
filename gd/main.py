import discord
import sys
import time

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
    
    client.run(token)
else:
    print("usage: python main.py [token]")
