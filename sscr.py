import os
import discord

TOKEN = ""
client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author.id == client.user.id and message.content == "bbpq":
        async for content in message.channel.history(limit=None).map(lambda m: m.content):
            if "discord.gg" in (content):
                print(content)
        print("finished")

client.run(TOKEN)
