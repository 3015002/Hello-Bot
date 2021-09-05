import discord
import os
import random
import numpy as np
from replit import db as db
import time as t

client = discord.Client()
cmd = db["cmdcount"]


@client.event
async def on_ready():
    #await client.change.presence(activity=discord.game('Hello!'))
    print('We have logged in as {0.user}!!!!!!'.format(client))
    print('AM PRO!!!')

    keys = db.keys()
    cmd = db["cmdcount"]
    print(keys)
    print(cmd)
    #cmdchat = np.str(cmd)
    t.sleep(30)
    #print(cmd)

    


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #hello cmd
    elif message.content.startswith(';hello'):
        await message.channel.send('Hello!')
        db["cmdcount"] += 1

    #hello cmd alt (;hi)
    elif message.content.startswith(';hi'):
        await message.channel.send('Hello!')
        db["cmdcount"] += 1

    #lotttery cmd
    elif message.content.startswith(';lottery'):
        lottery = random()
        lotmon = np.str(np.round(10000 * random()))
        if lottery > 0.4:
            await message.channel.send("You won " + lotmon + " dollars!")
            db["cmdcount"] += 1
        elif lottery < 0.4:
            await message.channel.send(
                "lol you didn't win the lottery better luck nest time!")
            db["cmdcount"] += 1

    #lottery cmd alt (;lot)
    elif message.content.startswith(';lot'):
        lottery = random()
        lotmon = np.str(np.round(10000 * random()))
        if lottery > 0.4:
            await message.channel.send("You won " + lotmon + " dollars!")
            db["cmdcount"] += 1
        elif lottery < 0.4:
            await message.channel.send(
                "lol you didn't win the lottery better luck nest time!")
            db["cmdcount"] += 1

    #flip heads cmd
    elif message.content.startswith(';flip heads'):
        flip = random()
        flipmoney = np.str(np.round(10000 * random()))
        if flip > 0.4:
            await message.channel.send("Heads! You won " + flipmoney +
                                       "  dollars!")
            db["cmdcount"] += 1
        elif flip < 0.4:
            await message.channel.send("Tails! You lost:(")
            db["cmdcount"] += 1

    #flip tails cmd
    elif message.content.startswith(';flip tails'):
        flip = random()
        if flip > 0.4:
            await message.channel.send("Heads! You lost;(")
            db["cmdcount"] += 1
        elif flip < 0.4:
            await message.channel.send("Tails! You Won " + flipmoney +
                                       " dollars!")
            db["cmdcount"] += 1
 
    #hunt cmd
    elif message.content.startswith(';hunt'):
      huntanimal = 'deer', 'rabbit', 'duck', 'skunk', ''
      huntthing = random.choice(huntanimal)
      await message.channel.send('You caught a ' + huntthing + '!' )
      db['cmdcount'] += 1

    #fish cmd
    elif message.content.startswith(';fish'):
      fish = random()
      if fish >0.4:
        await message.channel.send("You caught a fish!")
      elif fish <0.4:
        await message.channel.send("lol you caught nothing")

    #ping cmd
    elif message.content.startswith(';ping'):
        await message.channel.send('Pong!')
        db["cmdcount"] += 1

    #help cmd
    elif message.content.startswith(';help'):
        await message.channel.send(
            ";hello  ;lottery  ;flip <heads/tails>  ;ping  ;invite  ;info")
        db["cmdcount"] += 1

    #info cmd
    elif message.content.startswith(';info'):
        cmdchat = np.str(cmd)
        await message.channel.send('Creator: COOL GAMER #8269')
        await message.channel.send('Name: Hello Bot #8848')
        await message.channel.send('Code: Python 135 lines of code')
        await message.channel.send(
            'Coded with replit. Monitored using Uptimerobot')
        await message.channel.send("Commands issued: " + cmdchat + "")
        db["cmdcount"] += 1

    #invite cmd 
    elif message.content.startswith(';invite'):
        await message.channel.send(
            'Press this link to invite Hello Bot to your server! https://discord.com/oauth2/authorize?client_id=813376706161278986&scope=bot+applications.commands'
        )
        db["cmdcount"] += 1

    #invite cmd alt (;inv)
    elif message.content.startswith(';inv'):
        await message.channel.send(
            'Press this link to invite Hello Bot to your server! https://discord.com/oauth2/authorize?client_id=813376706161278986&scope=bot+applications.commands'
        )
        db["cmdcount"] += 1


client.run(os.getenv("TOKEN"))
