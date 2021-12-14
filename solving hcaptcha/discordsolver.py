import random
import discord
import time
import hcaptcha
import sys
from PIL import Image

TOKEN = "OTE4NDkxMDYzOTEwNTU1NjU4.YbIBdg.qNRcMxU3YJWePNkm4mQI8yhOdgE"
client = discord.Client()


def image_grid(imgs, rows, cols):
	assert len(imgs) == rows * cols
	
	w, h = imgs[0].size
	grid = Image.new('RGB', size=(cols * w, rows * h))
	grid_w, grid_h = grid.size
	
	for i, img in enumerate(imgs):
		grid.paste(img, box=(i % cols * w, i // cols * h))
	return grid

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	if message.content == "solvecaptcha":
		ch = hcaptcha.Challenge(
			site_key="f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34",
			site_url="https://discord.com/",
			#proxy="user:pass@127.0.0.1:8888",
			ssl_context=__import__("ssl")._create_unverified_context(),
			timeout=15
		)
		if ch.token:
			await message.channel.send(ch.token)
			return
		await message.channel.send(ch.question["en"])
		
		
		tilecount = 0
		challenges = []
		for tile in ch:
			challenges.append(tile)
			tilecount += 1
			image = tile.get_image(raw=True)
			with open(f'./images/my_image{str(tilecount)}.png', 'wb') as f:
				f.write(image)
		print(tilecount)
		tilecount = 0
		for tile in ch:
			tilecount += 1
			if tilecount == 1:
				images = [Image.open(x) for x in ['./images/my_image1.png', './images/my_image2.png', './images/my_image3.png',
				                                  './images/my_image4.png', './images/my_image5.png', './images/my_image6.png',
				                                  './images/my_image7.png', './images/my_image8.png', './images/my_image9.png']]
				grid = image_grid(images, rows=3, cols=3)
				grid.save('./images/test1.png')
				with open(f'./images/test1.png', 'rb') as f:
					picture = discord.File(f)
					await message.channel.send(content="answer (y/n) example: y y y n n n y y y (9 images)",
				                           file=picture)
				def check(m):
					return m.author == message.author
				
				msg = await client.wait_for("message", check=check)
				answers = msg.content.split(" ")
				currenttile = 0
				for answer in answers:
					currenttile += 1
					if answer == "y":
						ch.answer(challenges[currenttile])
			elif tilecount == 10:
				images = [Image.open(x) for x in
				          ['./images/my_image10.png', './images/my_image11.png', './images/my_image12.png',
				           './images/my_image13.png', './images/my_image14.png', './images/my_image15.png',
				           './images/my_image16.png', './images/my_image17.png', './images/my_image18.png']]
				grid = image_grid(images, rows=3, cols=3)
				grid.save('./images/test2.png')
				with open(f'./images/test2.png', 'rb') as f:
					picture = discord.File(f)
					await message.channel.send(content="answer (y/n) example: y y y n n n y y y (9 images)",
					                           file=picture)
				def check(m):
					return m.author == message.author
				
				msg = await client.wait_for("message", check=check)
				answers = msg.content.split(" ")
				currenttile = 0
				for answer in answers:
					currenttile += 1
					if answer == "y":
						ch.answer(challenges[currenttile+9])
		try:
			token = ch.submit()
			with open("token.txt", "wb") as f:
				f.write(bytes(token, "utf-8"))
			with open("token.txt", "rb") as f:
				file = discord.File(f)
				await message.channel.send(content="Here is your hcaptcha token", file=file)
		except hcaptcha.ChallengeError as err:
			await message.channel.send(err)


dorun = True

while dorun:
	try:
		client.run(TOKEN)
		dorun = False
	except:
		print("failed to login")
