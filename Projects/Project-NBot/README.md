# NBot

minecraft hivemind bot that if one person gets attacked, they will attack back in numbers

# TODO 
\
lumberjack command
\
self-defense for bots
\
mineflayer/discord.js communication
\
disable what the bot is doing before executing the command to prevent it from crashing
\
make the bot walk every 10 minutes to prevent it from getting disconnected and back to its original position
\
online mode version????? 

# h
\
https://github.com/PrismarineJS/mineflayer
\
\
it being used in game:\
https://www.youtube.com/watch?v=qJJU__idFao
\
\
what it should look like:\
https://www.youtube.com/watch?v=AYIcSEGx2EY

# Commands
all commands are only runnable by the botowner name\
You can also control the bot on https://localhost:5001 - https://localhost:5099 (meaning max 99 bots)\
command (args1) = required arguments\
command {args1} = not required but allowed\
\
say (message)\
    makes the bot chat the message\
\
bot comexyz (x) (y) (z)\
    makes the bot pathfind to the xyz coordinates\
\
bot come (botname), bot come all\
    makes the bot pathfind to your position\
\
eval (code)\
    runs a javascript code on the bot. if code errors, it will display in chat\
\
equiparmor\
    equips best armor. sometimes doesnt wear best armor\
\
bot roam\
    turns roaming on and off\
    walk randomly\
\
bot autofish\
    turns autofishing on and off\
    makes the bot look at water and start auto fishing\
\
bot attack (targetname)\
    attacks a player using the item currently held by the bot\
    for better effect, equip a weapon first\
\
equipblock (itemname)\
    equips an item onto the bot's hand\
\
throwblock (itemname)\
    drops an item from the bot's inventory\
\
tellinventory\
    tells what item is inside the bot's inventory

