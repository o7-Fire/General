import asyncio
import discord
import subprocess
import re
import os
import keep_alive
keep_alive.keep_alive()

TOKEN = "ODQxMjIxMDUwNTExMjYxNjk3.YJjmJw.iz2XBSsIQfDEjek4kWHQTKOxhZk"
client = discord.Client()
val = 0

f = open("val.txt", "r")
val = int(f.readlines()[0])
f.close()

def findcharlength(txtfile):
    with open(txtfile) as infile:
        words = 0
        characters = 0
        for lineno, line in enumerate(infile, 1):
            wordslist = line.split()
            words += len(wordslist)
            characters += sum(len(word) for word in wordslist)
    return characters
    
    
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
  if message.author.id == 0:
    return
  if message.author.bot:
    return
  if message.content == "test":
    await message.channel.send("yeah im alive")

  if message.content == "enablepr":
    global val
    if val != 0:
        val = 0
        f = open("val.txt", "w")
        f.write(str(val))
        f.close()
        await message.channel.send("printing each line disabled")
    else:
        val = 1
        f = open("val.txt", "w")
        f.write(str(val))
        f.close()
        await message.channel.send("printing each line enabled")
  if message.content.startswith("py"):
    if "while True" in message.content:
        await message.channel.send("<@" + str(message.author.id) + "> lmao no")
        return
    if "netsh" in message.content:
        await message.channel.send("<@" + str(message.author.id) + "> lmao no")
        return
    if "zipbomb" in message.content:
        await message.channel.send("<@" + str(message.author.id) + "> lmao no")
        return
    if "@everyone" in message.content:
        await message.channel.send("<@" + str(message.author.id) + "> lmao no")
        return
    if "@here" in message.content:
        await message.channel.send("<@" + str(message.author.id) + "> lmao no")
        return
    if 1 == 1:
      file_object  = open("pee.py", "w+")
      removedpy = message.content.replace("py", "", 1)
      calc = [m.start() for m in re.finditer("input()", removedpy)]
      for i in range(len(calc)):
          try:
              await message.channel.send("input:")
              msg = await client.wait_for("message", timeout=30)  # 30 seconds to reply
              removedpy = removedpy.replace("input()", str(msg.content), 1)
          except asyncio.TimeoutError:
              await message.channel.send("Sorry, you didn't reply in time!")
              return
      file_object.write(removedpy)
      file_object.close()
      std = subprocess.run(['python', 'pee.py'], capture_output=True, text=True)
      if "@everyone" in std.stdout:
        await message.channel.send("<@" + str(message.author.id) + "> lmao no")
      elif "@here" in std.stdout:
        await message.channel.send("<@" + str(message.author.id) + "> lmao no")
      elif "netsh" in message.content:
        await message.channel.send("<@" + str(message.author.id) + "> lmao no")
      else:
          if not std.stderr:
              if val == 1:
                  with open('assad.txt', 'w') as file:
                      file.write(std.stdout)
                  with open('assad.txt', 'r') as file:
                      msg = file.read(2000).strip()
                      while len(msg) > 0:
                          await message.channel.send(msg)
                          msg = file.read(2000).strip()
              else:
                    if len(std.stdout) >= 2000:
                        with open("result.txt", "w") as file:
                            file.write(std.stdout)
                        with open("result.txt", "rb") as file:
                            await message.channel.send("<@" + str(message.author.id) + "> Your file is:", file=discord.File(file, "result.txt"))
                    elif std.stdout == None:
                        await message.cannel.send("<@" + str(message.author.id) + "> no response")
                    else:
                        await message.channel.send("<@" + str(message.author.id) + ">")
                        await message.channel.send(std.stdout)
          else:
            await message.channel.send("Discord Error - " + str("none yet because nexity lazy") + '\n')
            await message.channel.send("Tracebacks:\n " + str(std.stderr))
    else:
      await message.channel.send("<@" + str(message.author.id) + "> no")

client.run(TOKEN)
