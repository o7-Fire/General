import asyncio
import sys

import discord
import subprocess
import re
import os

TOKEN = sys.argv[1]
client = discord.Client()
val = 0
whitelisted = [343591759332245505,  # nexity
               332394297536282634,  # ben
               450360653094584340,  # Volas
               394771663155101727, #gary
               102188661344321536, ]  # john
# 788246385988337664,
# 69347699700714706]
blacklistInput = {"@everyone", "@here", "netsh", "zipbomb", "blacklistOutput.txt"}
blacklistOutput = {"@everyone", "@here", "netsh", "zipbomb"}#thing you dont want to share
try:
    f = open("blacklistOuput.txt", 'r')
    for s in f.readlines():
        blacklistOutput.add(s)
    f.close()
except Exception:
    print("retard")
try:
    f = open("val.txt", "r")
    val = int(f.readlines()[0])
    f.close()
except Exception:
    print("retard")


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
    if message.author.bot:
        return
    if message.content == "test":
        await message.channel.send("yeah im alive")

    if message.content == "enablepr":
        global val
        if val != 0:
            val = 0
            valf = open("val.txt", "w")
            valf.write(str(val))
            valf.close()
            await message.channel.send("printing each line disabled")
        else:
            val = 1
            valf = open("val.txt", "w")
            valf.write(str(val))
            valf.close()
            await message.channel.send("printing each line enabled")
    if message.content.startswith("python") and not message.content.upper() in (b.upper() for b in blacklistInput):
        if len(str(message.content).split(" ", 1)) < 1:
            await message.channel.send("not enough arg")
            return
        executor: str = message.content.split(" ", 1)[0]
        if whitelisted.count(message.author.id) > 0:
            file_object = open("pee.py", "w+")
            parsed = message.content.replace(executor+" ", "", 1)
            calc = [m.start() for m in re.finditer("input()", parsed)]
            for i in range(len(calc)):
                try:
                    await message.channel.send("input:")
                    msg = await client.wait_for("message", timeout=30)  # 30 seconds to reply
                    parsed = parsed.replace("input()", str(msg.content), 1)
                except asyncio.TimeoutError:
                    await message.channel.send("Sorry, you didn't reply in time!")
                    return
            file_object.write(parsed)
            file_object.close()
            std: subprocess = None
            try:
                std = subprocess.run([executor, 'pee.py'], capture_output=True, text=True)
                for b in blacklistOutput:
                    b = b.upper()
                    if b in std.stdout.upper() or TOKEN.upper() in std.stdout.upper():
                        await message.channel.send("<@" + str(message.author.id) + "> lmao no")
                        return
            except FileNotFoundError:
                await message.channel.send("no executor found")

            if std is None:
                return

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
                            await message.channel.send("<@" + str(message.author.id) + "> Your file is:",
                                                       file=discord.File(file, "result.txt"))
                    elif std.stdout is None:
                        await message.cannel.send("<@" + str(message.author.id) + "> no response")
                    else:
                        await message.channel.send("<@" + str(message.author.id) + ">")
                        await message.channel.send(std.stdout)
            else:
                await message.channel.send("Discord Error - " + str("none yet because nexity lazy") + '\n')
                await message.channel.send("Tracebacks:\n " + str(std.stderr))
        else:
            await message.channel.send("<@" + str(message.author.id) + "> lmao no")


# from keep_alive import keep_alive

# keep_alive()
client.run(TOKEN)
