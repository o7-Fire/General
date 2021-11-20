import os
try:
  os.system("pip3 install discum")
  import discum
except:
  print("h")
bot = discum.Client(token=os.getenv("TOKEN1"))

def close_after_fetching(resp, guild_id):
	if bot.gateway.finishedMemberFetching(guild_id):
		lenmembersfetched = len(bot.gateway.session.guild(guild_id).members) #this line is optional
		print(str(lenmembersfetched)+' members fetched') #this line is optional
		bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
		bot.gateway.close()

def get_members(guild_id, channel_id):
	bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1) #get all user attributes, wait 1 second between requests
	bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
	bot.gateway.run()
	bot.gateway.resetSession() #saves 10 seconds when gateway is run again
	return bot.gateway.session.guild(guild_id).members

members = get_members('374718301063872542', '677631780857184313')
with open("members.txt", "a") as f:
	for member in members:
		f.write("\n" + member)
