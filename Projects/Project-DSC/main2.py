import discord
import requests
import threading
import time

TOKEN = ""
client = discord.Client()

def getpage(ids, page):
	try:
		r = requests.get("https://discordapp.com/api/v9/guilds/" + ids + "/messages/search?has=link&offset=" + str(page * 25), headers={'authorization': TOKEN})
		for messages in r.json()["messages"]:
			themessage = messages[0]
			#print(themessage["content"])
			if "discord.gg/" in themessage["content"]:
				print((f"https://discord.gg/{themessage['content'].split('discord.gg/')[1].split(' ')[0]}"))
	except:
		asdsdfsdgsdg = 0
			
@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	if message.author.id != client.user.id:
		return
	if "zxc " in message.content:
		ids = message.content.split("zxc ")[1]
		for i in range(2000):
			t = threading.Thread(target=getpage, args=(ids, i))
			t.start()
			time.sleep(0.1)
			
client.run(TOKEN)
