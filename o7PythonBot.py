import asyncio
import sys

import discord
import subprocess
import re
import os
import time

from discord.ext.commands import bot

TOKEN = sys.argv[1]
client = discord.Client()
val = 0
whitelisted = [343591759332245505,  # nexity
               332394297536282634,  # ben
               450360653094584340,  # Volas
               394771663155101727,  # gary
               102188661344321536, ]  # john
# 788246385988337664,
# 69347699700714706]
blacklistInput = {"@everyone", "@here", "netsh", "zipbomb", "blacklistOutput.txt"}
blacklistOutput = {"@everyone", "@here", "netsh", "zipbomb"}  # thing you dont want to share
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


def millis():
    return round(time.time() * 1000)


def blacklistedO(s: str):
    for b in blacklistOutput:
        b = b.upper()
        if b in s.upper() or TOKEN.upper() in s.upper():
            return True
    return False


import contextlib
import io

eval('print("you are")')





@client.event
async def on_message(message):
    global val
    if message.author.bot:
        return
    if message.content == "test":
        await message.channel.send("yeah im alive")

    if message.content == "enablepr":
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
    if (message.content.startswith("python") or message.content.startswith("pip")) and not message.content.upper() in (
            b.upper() for b in blacklistInput):
        executor: str
        extra: chr
        if len(str(message.content).split('\n', 1)) > 1:
            executor = message.content.split('\n', 1)[0]
            extra = '\n'
        elif len(str(message.content).split(" ", 1)) > 1:
            executor = message.content.split(' ', 1)[0]
            extra = ' '
        else:
            await message.channel.send("no arg")
            return

        if whitelisted.count(message.author.id) > 0:
            file_object = open("pee.py", "w+")
            parsed = message.content.replace(executor + extra, "", 1)
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
                print(message.content)
                if executor.startswith("pip"):
                    std = subprocess.run(str(message.content).split(" "), capture_output=True, text=True)
                else:
                    std = subprocess.run([executor, 'pee.py'], capture_output=True, text=True)
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
                        last: int
                        while len(msg) > 0:
                            if blacklistedO(msg):
                                await message.channel.send("<@" + str(message.author.id) + "> lmao no")
                            else:
                                last = millis()
                                await message.channel.send(msg)
                            msg = file.read(2000).strip()
                else:
                    if len(std.stdout) >= 2000:
                        with open("result.txt", "w") as file:
                            if blacklistedO(std.stdout):
                                await message.channel.send("<@" + str(message.author.id) + "> lmao no")
                                return
                            else:
                                file.write(std.stdout)
                        with open("result.txt", "rb") as file:
                            await message.channel.send("<@" + str(message.author.id) + "> Your file is:",
                                                       file=discord.File(file, "result.txt"))
                    elif std.stdout is None:
                        await message.cannel.send("<@" + str(message.author.id) + "> no response")
                    else:
                        await message.channel.send("<@" + str(message.author.id) + ">")
                        if blacklistedO(std.stdout):
                            await message.channel.send("<@" + str(message.author.id) + "> lmao no")
                            return
                        await message.channel.send(std.stdout)
            else:
                await message.channel.send("Discord Error - " + str("none yet because nexity lazy") + '\n')
                if blacklistedO(std.stderr):
                    await message.channel.send("<@" + str(message.author.id) + "> lmao no")
                    return
                await message.channel.send("Tracebacks:\n " + str(std.stderr))
        else:
            await message.channel.send("<@" + str(message.author.id) + "> lmao no")


# from keep_alive import keep_alive

# keep_alive()
client.run(TOKEN)
