from datetime import datetime
import os
import discord


client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        print("connected to guild %s" % guild)

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # ignore messages sent by the bot

    now = datetime.now()

    words = message.content.split(" ")
    if words[0] == "!date":
        result=("%02d/%02d/%04d %02d:%02d:%02d" % (now.day, now.month, now.year, now.hour, now.minute, now.second))
        await message.channel.send(result)

client.run(os.getenv('DISCORD_TOKEN'))
