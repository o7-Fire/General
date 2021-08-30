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
			if len(getguildbyid(theserver).members) >= 1000:
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
						n = 1900
						flist = [totalinvitesgained[i:i + n] for i in range(0, len(totalinvitesgained), n)]
						for below2000 in flist:
							await webhook.send("```from: " + textchannel.name + "\n" + below2000 + "```")
						totalinvitesgained = ""
						
			else:
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
					n = 1900
					flist = [totalinvitesgained[i:i + n] for i in range(0, len(totalinvitesgained), n)]
					for below2000 in flist:
						await webhook.send("```" + below2000 + "```")
		else:
			theinvite = int(message.content.split("gaininvites ")[1])
			totalinvitesgained = ""
			print("got guild successfully")
			if len(getguildbyid(theinvite).members) >= 1000:
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
						n = 1900
						flist = [totalinvitesgained[i:i + n] for i in range(0, len(totalinvitesgained), n)]
						for below2000 in flist:
							await webhook.send("```from: \n" + textchannel.name + below2000 + "```")
						totalinvitesgained = ""
			else:
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
					n = 1900
					flist = [totalinvitesgained[i:i + n] for i in range(0, len(totalinvitesgained), n)]
					for below2000 in flist:
						await webhook.send("```" + below2000 + "```")

client.run(TOKEN)
