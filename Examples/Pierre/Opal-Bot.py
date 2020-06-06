import discord
from discord.ext import commands, tasks
import os
import random
from itertools import cycle
from flask import ctx
import requests, json

client = commands.Bot(command_prefix=".")

status = cycle(["DM @PierreCam#6969 to add me to your server!", "Listening to your commands!"])


@client.event
async def on_ready():
    status_loop.start()
    await client.change_presence(
        status=discord.Status.online)  # , activity=discord.Game("Online")) UNCOMMENT IF WANT A NON LOOPING STATUS
    print("Bot is ready and connected to the following guilds:")
    for guild in client.guilds:
        print("Guild name: %s" % guild)


@tasks.loop(seconds=30)
async def status_loop():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_member_remove(member):
    print(f"{member} has left or been removed from a Server")


@client.command()
async def ping(ctx):
    await ctx.send(f"The Ping is at: {round(client.latency * 1000)} ms")


@client.command()
async def weather(ctx, *, city):
    api_key = "WEATHER_API_KEY"

    base_url = "http://api.openweathermap.org/data/2.5/weather?appid=310b950bcd05029af4e22e41ca2315ed&q"

    city_name = city

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":

        y = x["main"]

        current_temperature = y["temp"]
        temp_centigrade = current_temperature - 273.15
        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]

        await ctx.send(f"**Temperature:** {round(temp_centigrade)}°C")
        await ctx.send(f" **Atmospheric Pressure:** {current_pressure} hPa")
        await ctx.send(f" **Humidity:** {current_humidity}%")
        await ctx.send(f" **Weather Description:** {weather_description}")
    else:
        await ctx.send("City Not Found")


@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
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
    await ctx.send(f"{random.choice(responses)}")


@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} has been kicked from a server for {reason}")


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} has been banned from a server for: {reason}")


@client.command()
async def test(ctx):
    await ctx.send("Bot is running Fine!")


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return


@client.command()
async def gay(ctx, *, member):
    responses = [
        f"Yes, {member} is very gay",
        f"{member} is the gayest of the gayest",
        f"{member} = Gay",
        f"Hahaha, Gay {member}",
        f"{member} is the gayest there is no doubt about that"
    ]
    await ctx.send(f"{random.choice(responses)}")

@client.command()
async def gayrate(ctx, *, member):
    responses = random.randint(1, 100)
    await ctx.send(f"{member} is {responses}% gay")

# FIX LATER
# @client.command()
# async def join(ctx):
#    author = ctx.message.author
#    channel = author.voice_channel
#    await client.join_voice_channel(channel)


@weather.error
async def weather_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please use the format: `.weather {Insert Location}`")


@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please use the format: `.8ball {insert question}`")


@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify the amount of messages you want to be purged")


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify the user you want to kick")


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify the user you want to ban")


# FIX LATER
# @unban.error()
# async def unban_error(ctx, error):
#    if isinstance(error, commands.MissingRequiredArgument):
#       await ctx.send("Please specify the user you want to unban")


# @client.event()
# async def on_command_error(ctx, error):
#   if isinstance(error, commands.CommandNotFound):
#      await ctx.send("Command does not exist")


client.run(os.getenv('TOKEN'))
