import time
import threading
import requests
import random
import csv
from fake_headers import Headers

header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate ony Windows platform
    headers=True  # generate misc headers
)
	    
min = 0
max = 29000000 #latest account 2.9 bil
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
with open("proxies.txt", "r") as proxyx:
	proxies = proxyx.read().split("\n")

def write(message):
	with open('result.csv', mode='a') as f:
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(message)
	
for abasrbaebwa in range(500):
	def newthread(threadcxount):
		
		while True:
			https_proxy = random.choice(proxies)
			
			proxyDict = {
			  "http"  : https_proxy,
			  "https" : https_proxy
			}
			#print("using " + str(https_proxy))
			
			thenum = random.randint(min, max)
			finalmessage = ""
			userids2 = str((thenum + 1) * 100 + 1)
			userids = str((thenum + 1)*100 + 1)
			for x in range(99):
				userids += "%2C" + str((x + 1) + (thenum + 1)*100 + 1)
			api = f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={userids}&size=48x48&format=Png&isCircular=false"
			#https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds=500555555%2C500555556&size=48x48&format=Png&isCircular=false
			#refer to this
			isproxygood = True
			try:
				r = requests.get(api, headers=header.generate(), proxies=proxyDict)
				
				if isproxygood:
					ther = r.json()
					didratelimit = True
					try:
						bhdfbh = ther["data"]
						didratelimit = False
					except:
						print("ratelimited")
						time.sleep(30)
						
					if didratelimit == False:
						for d in ther["data"]:
							cantry = True
							try:
								int(d['targetId']) + 1
							except:
								cantry = False
							if cantry:
								write([d['targetId'], d['imageUrl']])
						print("done " + userids2)
			except:
				print("request failed")

	t1 = threading.Thread(target=newthread, args=(abasrbaebwa,))
	t1.start()
	print("thread created: " + str(abasrbaebwa))
