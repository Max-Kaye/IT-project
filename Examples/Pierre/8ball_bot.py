import random
import os
import discord
import requests

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
        def check(amessage):
            return amessage.author == message.author

        mention = message.author.mention
        result = f"Hi {mention} Ask me a yes or no question"
        await message.channel.send(result)
        await client.wait_for("message", check=check)
        result = random.choice(responses)
        await message.channel.send(result)

    if message.content.startswith("!badbot"):
        mention = message.author.mention
        result = f"Sorry, Master {mention}"
        await message.channel.send(result)


client.run(os.getenv('TOKEN'))