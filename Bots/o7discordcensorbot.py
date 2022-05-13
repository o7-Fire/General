import traceback

import keep_alive
keep_alive.keep_alive()

import dialogflow
from google.api_core.exceptions import InvalidArgument
import os
import discord
import unicodedata
import json
import sys
import urllib.request
import requests
import operator
import re
from monkeylearn import MonkeyLearn

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


isTextCensorEnabled = 0
isSpamAllowed = 0
try:
    with open("spamsettings.txt", "r+") as f:
        isSpamAllowed = f.read()
except FileNotFoundError:
    print("hey spamsettings.txt is not found")
try:
    with open("textcensorsettings.txt", "r+") as f:
        isSpamAllowed = f.read()
except FileNotFoundError:
    print("hey textcensorsettings.txt is not found")

print("VALUE OF ISSPAMALLOWED: " + str(isSpamAllowed))
print("VALUE OF ISTEXTCENSORENABLED: " + str(isTextCensorEnabled))
ml = MonkeyLearn(os.getenv('ML_TOKEN'))
TOKEN = os.getenv('BOT_TOKEN')  # for now use glitch api since volas having problem
##https://o7-api.glitch.me
##https://o7inc.ddns.net
o7API = "https://o7-api.glitch.me"  # choose your api
client = discord.Client()  # finally migrated to o7inc.ddns.net api
spam = {}
maxhandleReadableContent = 0.25  # 0 - 1. read async def handleReadableContent
threshold = 0.62  # anything higher than this get vetoed
thresholdMinimizer = 0.25  # to sum up with other value
thresholdNeutralizer = 0.017  # round to 0 automatically
thresholdMaximizer = 0.81  # if the index above this and is safe dont delete
safeIndex = ["Neutral"]  # prevent false positive, never trust Drawing
neutralIndex = ['Neutral']#Not worth checking
badIndex = ["Porn", "Sexy", "Hentai", "Anime"]
censored_words = ["suck me", "suck ne", "masterbat",
                  "horny", "lesbian", "bisexual", "vagina", "penis", "cock", "mastorbat",
                  "hentai", "henthai", "hxntai", "hormy", "fuck ne", "masturbat",
                  "lets sex", "porn", "daddy", "porm", "fuck me", "anal", "buttplug",
                  ":woozy_face:", ":flushed:", ":drooling_face:", "rape"]  # 343591759332245505
whitelisted_users = [7706075274265231707, 753874678220849174, 332394297536282634]
urlDiscordMedia = re.compile("((https|http):\/\/[0-9a-zA-Z\.\/_-]+.(png|jpg|gif|webm|mp4|jpeg))")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'

DIALOGFLOW_PROJECT_ID = os.getenv('PROJECT_ID')
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


def getClassification(img: str):
    content = keep_alive.fetch(o7API + '/api/json/graphical/classification/' + img)  
    return json.loads(content)

#weeb problems require weeb solution
async def handleReadableContent(message, content: str, value: float, debug: bool):
  deleted: bool = False
  msg: str = "contain"
  aftercontent: str = ""
  print(str(value) + " > " + str(threshold))
  if value > threshold:
    if badIndex.__contains__(content):#keep shit simple
        await message.delete()
        deleted = True
        aftercontent = aftercontent + " and moderated"
  else:
    msg = "probably " + msg
  if debug: #fuck you
    msg = " is red pilled and " + msg
  if deleted or debug:
      await message.channel.send('<@' + str(message.author.id) + f'> We have found that your attachment {msg} ** {content} **{aftercontent} :  {str(value)}')
  return deleted#get moderated

#WTF HAPPENED lmao same
#wtf i just get tped
def checkvideotype(name, prefix):
    filename = name[-len(prefix) - 1:]
    if filename == f'.{prefix}':
        return True


def aboveLimit(val: float):
    return val > threshold


def neutralize(contents: dict, key: str, target: str):
    if contents[key] < thresholdNeutralizer:
        contents[target] = 0
    if contents[key] > 1 - thresholdNeutralizer:
        contents[target] = 0
    if contents[key] < thresholdMinimizer:
        contents[target] = contents[target] - thresholdMinimizer


async def checkVisual(message):
    if message.channel.nsfw:
        return
    urls: list = urlDiscordMedia.findall(message.content)
    done: list = []
    for img in message.attachments:
        if done.__contains__(img): continue
        done.append(img)
        if await checkVisualF(message, img.url):
            return True
    for u in urls:
        if done.__contains__(u[0]): continue
        done.append(u[0])
        if await checkVisualF(message, u[0]):
            return True
    return False


async def checkVisualF(message, img):
    try:
        debug = "debug" in message.content
        rawResponse: dict = getClassification(img)  # json parser from api
        contents: dict = rawResponse.copy()
        contents["model"] = 0
        contents = dict(sorted(contents.items(), key=operator.itemgetter(1), reverse=True))  # sort float value
        fancycontent = str(contents).replace(",", "\n").replace("{", "").replace("}", "").replace("'", "").replace(" ", "")
        readablecontents = fancycontent.split("\n")
        fixedcontent = ""
        for gayb in readablecontents:
            a = gayb.split(":")
            fixedcontent = fixedcontent + "\n" + a[0] + " : " + a[1]
        if debug:  # does it good now
            print("debug")
            await message.channel.send(fixedcontent + "\n" + str(rawResponse["model"]))
        #True positive
        if not debug:
          print("not debug")
          for sf in safeIndex:
             if contents[sf] > thresholdMaximizer:
                  return False
        debugThershold: float = thresholdMaximizer - threshold
        debugThershold = threshold - debugThershold
        outcome: bool = False
        for sf in contents.items():##For each item
            print(str(sf))
            if neutralIndex.__contains__(sf[0]) and not debug: continue #if this neutral continue
            if sf[1] > threshold or (debug and sf[1]> debugThershold):
                print("exceeded" + sf[0] + str(sf[1]))
                await handleReadableContent(message, sf[0], sf[1], debug)#Wether to be deleted or not
                outcome = True #moderated 
        return outcome #pass moderated
    except Exception as e:
        print("no image found")
        traceback.print_exc()
        print("stackerror: " + str(e))
        return False


async def basicHandle(message):
    print("VV---------------------------------------------VV")
    print(message.author.name + ": " + message.content)
    try:
        img = message.attachments[0].url
        print(message.author.name + ": " + img)
    except:
        a = 0
    print("^^---------------------------------------------^^")
    if message.content == "test":
        await message.channel.send("assadn't")
    if message.author.id in whitelisted_users or message.author.id == 343591759332245505:
        if message.content == "restartbot":
            await message.channel.send("restarting")
            restart_program()
        return


async def checkSpam(message):
    global isSpamAllowed
    print("the spam : " + str(isSpamAllowed))
    if isSpamAllowed == 1:
        return False
    try:
        if message.content.lower() == spam[message.author.id]:
            await message.delete()
            # channel = await message.author.create_dm()
            # await channel.send("stop spamming")
            # do i need to block the bots  |  yes you do
            return True
    except:
        print("oh noes")
    finally:
        spam[message.author.id] = message.content.lower()
    return False

async def handleBot(message):
 if message.channel.id == 815743358639013958:
      contents = requests.get(f'https://api.affiliateplus.xyz/api/chatbot?message={message.content}&botname=o7 AI Bot&ownername=Nexity&user=1').text
      cleanup = contents.split(":")[1].replace('"', "").replace("}", "")
      await message.channel.send(cleanup)

async def handleText(message):
  content = message.content
  model_id = 'cl_fobQ7iGo'
  data = [content]
  result = ml.classifiers.classify(model_id, data)
  for items in result.body:
    for item in items['classifications']:
      #await message.channel.send(str(item) + str(type(item)))
      if item['tag_name'] == "NSFW":
        await message.channel.send(f'<@{message.author.id}> Your message was detected to be {item["tag_name"]}\nProbability {item["confidence"]}')
        
async def handleTextG(message):
  text_to_be_analyzed = message.content

  session_client = dialogflow.SessionsClient()
  session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
  text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
  query_input = dialogflow.types.QueryInput(text=text_input)
  try:
      response = session_client.detect_intent(session=session, query_input=query_input)
  except InvalidArgument:
      raise

  if response.query_result.intent.display_name == "NSFW intent":
    if response.query_result.intent_detection_confidence > 0.5:
      await message.delete()
      await message.channel.send(f"""<@{message.author.id}> Your message was checked and is probably NSFW
Detected intent confidence:  {response.query_result.intent_detection_confidence}""")
    else:
      await message.channel.send(f"""<@{message.author.id}> Your message was checked and is maybe NSFW
Detected intent confidence:  {response.query_result.intent_detection_confidence}""")


@client.event
async def on_message(message):
    global isSpamAllowed
    global isTextCensorEnabled
    if message.author.id == 0:  # if you hate someone really bad and you cant ban him from a server because the state doesnt let you
        await message.delete()

    if message.author.bot:
        return
    # DONT DELETE
    await basicHandle(message)
    await handleBot(message)
    #try:
    #  await handleText(message)
    #except:
    #  a = 1
    await handleTextG(message)

    if message.content == "switchspam":
        if message.author.id in whitelisted_users or message.author.id == 343591759332245505:
            if isSpamAllowed:
                isSpamAllowed = 0
                with open("spamsettings.txt", "w+") as f:
                    f.write(str(isSpamAllowed))
                await message.channel.send("turned on antispam")
            else:
                isSpamAllowed = 1
                with open("spamsettings.txt", "w+") as f:
                    f.write(str(isSpamAllowed))
                await message.channel.send("turned off antispam")

    if message.content == "switchtextcensor":
        if message.author.id in whitelisted_users or message.author.id == 343591759332245505:
            if isTextCensorEnabled:
                isTextCensorEnabled = 0
                with open("textcensorsettings.txt", "w+") as f:
                    f.write(str(isTextCensorEnabled))
                await message.channel.send("turned on chat censor")
            else:
                isTextCensorEnabled = 1
                with open("textcensorsettings.txt", "w+") as f:
                    f.write(str(isTextCensorEnabled))
                await message.channel.send("turned off chat censor")

    if "is AFK" in message.content and message.author.id == 155149108183695360:
        await message.delete()

    if message.author.id in whitelisted_users and not str(message.content).startswith("debug"):
        return

    if not message.content == "debug":
        if await checkSpam(message):
            return

    if await checkVisual(message):
        return

    #for words in censored_words:
        #if message.channel.nsfw:
        #    return
        #if isTextCensorEnabled == 1:
        #    return
        #msg = message.content.lower().replace("0", "o").replace("4", "a").replace("3", "e").replace("@", "o").replace(
        #    "1", "l").replace(".", "").replace(" ", "")
        #if words in unicodedata.normalize('NFKC', msg):
        #    await message.delete()
        #    await message.channel.send("get censored")


if __name__ == '__main__':
    client.run(TOKEN)
