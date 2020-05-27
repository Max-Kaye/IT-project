import random
import os
import discord

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        print("connected to guild %s" % guild)

responses = [
    "It is certain",
    "Without a doubt",
    "You may rely on it",
    "Yes definitely",
    "It is decidedly so",
    "As I see it, yes",
    "Most likely",
    "Yes",
    "Signs point to yes",
    "Better not tell you now",
    "Ask again later",
    "Cannot predict now",
    "Concentrate and ask again",
    "My sources say no",
    "My reply is no"
]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!8ball"):
        result = "What is your Yes or No question?"
        await message.channel.send(result)
        if message.content == result:
            return
        else:
            result = random.choice(responses)
            await message.channel.send(result)



client.run(os.getenv('DISCORD_TOKEN'))
