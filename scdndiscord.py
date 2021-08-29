import requests

filewithyourcdnlinks = "textfile.txt"
with open(filewithyourcdnlinks, "r") as f:
	t = f.read().split("\n")
	for links in t:
		theembedname = links.split("/")[6]
		with open(theembedname, "wb+") as file:
			file.write(requests.get(links).content)
