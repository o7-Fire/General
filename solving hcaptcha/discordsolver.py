import random
import discord
import time

TOKEN = ""
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content == "solvecaptcha":
        import hcaptcha
        time.sleep(10)
        ch = hcaptcha.Challenge(
            site_key="f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34",
            site_url="https://discord.com/",
            # proxy="user:pass@127.0.0.1:8888",
            # ssl_context=__import__("ssl")._create_unverified_context(),
            timeout=10
        )
        if ch.token:
            await message.channel.send(ch.token)
            return
        await message.channel.send(ch.question["en"])

        for tile in ch:
            image = tile.get_image(raw=True)
            with open('my_image.png', 'wb') as f:
                f.write(image)
            with open('my_image.png', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(content="answer (y/n):", file=picture)

            def check(m):
                return m.author == message.author
            msg = await client.wait_for("message", check=check)
            if msg.content == "y":
                ch.answer(tile)

        try:
            token = ch.submit()
            with open("token.txt", "wb") as f:
                f.write(bytes(token, "utf-8"))
            with open("token.txt", "rb") as f:
                file = discord.File(f)
                await message.channel.send(content="Here is your hcaptcha token", file=file)
        except hcaptcha.ChallengeError as err:
            await message.channel.send(err)
            
client.run(TOKEN)
