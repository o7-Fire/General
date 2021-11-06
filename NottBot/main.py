import time
import threading
import requests
import random

min = 0
max = 2900000000 #latest account 2.9 bil
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
with open("proxies.txt", "r") as proxyx:
	proxies = proxyx.read().split("\n")
	
for abasrbaebwa in range(100):
	def newthread(threadcxount):
		while True:
			https_proxy = random.choice(proxies)
			
			proxyDict = {
			  "http"  : https_proxy,
			  "https" : https_proxy
			}
			print("using " + str(https_proxy))
			
			thenum = random.randint(min, max)
			finalmessage = ""
			userids = str((thenum + 1)*100 + 1)
			for x in range(99):
				userids += "%2C" + str((x + 1) + (thenum + 1)*100 + 1)
			api = f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={userids}&size=48x48&format=Png&isCircular=false"
			#https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds=500555555%2C500555556&size=48x48&format=Png&isCircular=false
			#refer to this
			isproxygood = True
			r = requests.get(api, headers=headers, proxies=proxyDict)
			
			if isproxygood:
				ther = r.json()
				didratelimit = True
				try:
					bhdfbh = ther["data"]
					didratelimit = False
				except:
					print("ratelimited")
					time.sleep(10)
					
				if didratelimit == False:
					for d in ther["data"]:
						cantry = True
						try:
							int(d['targetId']) + 1
						except:
							cantry = False
						if cantry:
							finalmessage += f"{d['targetId']} {d['imageUrl']}\n"
					with open("result.txt", "a") as f:
						f.write(finalmessage)

	t1 = threading.Thread(target=newthread, args=(abasrbaebwa,))
	t1.start()
	print("thread created: " + str(abasrbaebwa))
