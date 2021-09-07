import string
import random
def split(word):
    return [char for char in word]
result = split(string.ascii_letters) + [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def gen(num):
 finalmessage = ""
 for i in range(num):
  finalmessage = finalmessage + str(random.choice(result))
 return finalmessage
def genlink(num):
 finalmessage = ""
 for i in range(num):
  finalmessage = finalmessage + "discord.gg/" + gen(10) + "\n"
 return finalmessage
print(genlink(10))
