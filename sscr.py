# dont be dumb like me, use it on an account that is phone verified or join one server every few minutes (if not your account gets phone locked)

import discord
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import requests
import time

TOKEN = ""
WEBHOOK = ""
client = discord.Client()
theserver = 0

def getguildbyid(theid):
	for guild in client.guilds:
		if guild.id == theid:
			return guild
@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	global theserver
	if message.author.id == client.user.id and message.content == "bbpq":
		async for content in message.channel.history(limit=None).map(lambda m: m.content):
			if "discord.gg/" in (content):
				print(f"https://discord.gg/{content.split('discord.gg/')[1].split(' ')[0]}")
		print("finished")
	
	if message.author.id == client.user.id and "joinserver " in message.content:
		theinvite = message.content.split("joinserver ")[1]
		r = requests.post("https://discordapp.com/api/v6/invites/" + theinvite, headers={'authorization': TOKEN})
		time.sleep(8)
		theguildjoinedid = int(r.text.split('id": "')[1].split('", "name')[0])
		theserver = theguildjoinedid
		print("joined successfully")
	
	if message.author.id == client.user.id and "gaininvites" in message.content:
		if message.content == "gaininvites":
			totalinvitesgained = ""
			print("got guild successfully")
			for textchannel in getguildbyid(theserver).text_channels:
				try:
					async for content in textchannel.history(limit=None).map(lambda m: m.content):
						if "discord.gg/" in (content):
							totalinvitesgained = totalinvitesgained + (
								f"https://discord.gg/{content.split('discord.gg/')[1].split(' ')[0]}") + "\n"
				except:
					afvuiwfuibwtuivw = 0
			async with aiohttp.ClientSession() as session:
				webhook = Webhook.from_url(WEBHOOK, adapter=AsyncWebhookAdapter(session))
				await webhook.send("```" + totalinvitesgained + "```")
		else:
			theinvite = int(message.content.split("gaininvites ")[1])
			totalinvitesgained = ""
			print("got guild successfully")
			for textchannel in getguildbyid(theinvite).text_channels:
				try:
					async for content in textchannel.history(limit=None).map(lambda m: m.content):
						if "discord.gg/" in (content):
							totalinvitesgained = totalinvitesgained + (
								f"https://discord.gg/{content.split('discord.gg/')[1].split(' ')[0]}") + "\n"
				except:
					afvuiwfuibwtuivw = 0
			async with aiohttp.ClientSession() as session:
				webhook = Webhook.from_url(WEBHOOK, adapter=AsyncWebhookAdapter(session))
				await webhook.send("```" + totalinvitesgained + "```")


client.run(TOKEN)
