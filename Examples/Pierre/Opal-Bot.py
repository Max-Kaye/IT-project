from textwrap import indent
import discord
from discord import guild
from discord.ext import commands, tasks
import os
import random
from itertools import cycle
from flask import ctx
import requests, json
import urbandict
import functools
import itertools
import asyncio
import math
import youtube_dl
from async_timeout import timeout
import pickle
from datetime import datetime
import pyowm
import json

client = commands.Bot(command_prefix=".")

status = cycle(["DM @PierreCam#6969 to add me to your server!", "Listening to your commands!",
                "NOTE, THIS BOT IS STILL IN AN ALPHA DEVELOPEMENT STAGE."])


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
    pingembed = discord.Embed(
        colour=discord.Colour.dark_magenta(),
        description=f"The Ping is at: {round(client.latency * 1000)} ms",
    )
    await ctx.send(embed=pingembed)


Icons = {
    # thunderstorm
    "thunderstorm with light rain": "http://openweathermap.org/img/wn/11d@2x.png",
    "thunderstorm with rain": "http://openweathermap.org/img/wn/11d@2x.png",
    "thunderstorm with heavy rain": "http://openweathermap.org/img/wn/11d@2x.png",
    "light thunderstorm": "http://openweathermap.org/img/wn/11d@2x.png",
    "thunderstorm": "http://openweathermap.org/img/wn/11d@2x.png",
    "heavy thunderstorm": "http://openweathermap.org/img/wn/11d@2x.png",
    "ragged thunderstorm": "http://openweathermap.org/img/wn/11d@2x.png",
    "thunderstorm with light drizzle": "http://openweathermap.org/img/wn/11d@2x.png",
    "thunderstorm with drizzle": "http://openweathermap.org/img/wn/11d@2x.png",
    "thunderstorm with heavy drizzle": "http://openweathermap.org/img/wn/11d@2x.png",
    # drizzle
    "light intensity drizzle": "http://openweathermap.org/img/wn/09d@2x.png",
    "drizzle": "http://openweathermap.org/img/wn/09d@2x.png",
    "heavy intensity drizzle": "http://openweathermap.org/img/wn/09d@2x.png",
    "light intensity drizzle rain": "http://openweathermap.org/img/wn/09d@2x.png",
    "drizzle rain": "http://openweathermap.org/img/wn/09d@2x.png",
    "heavy intensity drizzle rain": "http://openweathermap.org/img/wn/09d@2x.png",
    "shower rain and drizzle": "http://openweathermap.org/img/wn/09d@2x.png",
    "heavy shower rain and drizzle": "http://openweathermap.org/img/wn/09d@2x.png",
    "shower drizzle": "http://openweathermap.org/img/wn/09d@2x.png",
    # rain
    "light rain": "http://openweathermap.org/img/wn/10d@2x.png",
    "moderate rain": "http://openweathermap.org/img/wn/10d@2x.png",
    "heavy intensity rain": "http://openweathermap.org/img/wn/10d@2x.png",
    "very heavy rain": "http://openweathermap.org/img/wn/10d@2x.png",
    "extreme rain": "http://openweathermap.org/img/wn/10d@2x.png",
    "freezing rain": "http://openweathermap.org/img/wn/13d@2x.png",
    "light intensity shower rain": "http://openweathermap.org/img/wn/09d@2x.png",
    "shower rain": "http://openweathermap.org/img/wn/09d@2x.png",
    "heavy intensity shower rain": "http://openweathermap.org/img/wn/09d@2x.png",
    "ragged shower rain": "http://openweathermap.org/img/wn/09d@2x.png",
    # snow
    "light snow": "http://openweathermap.org/img/wn/13d@2x.png",
    "Snow": "http://openweathermap.org/img/wn/13d@2x.png",
    "Heavy snow": "http://openweathermap.org/img/wn/13d@2x.png",
    "Sleet": "http://openweathermap.org/img/wn/13d@2x.png",
    "Light shower sleet": "http://openweathermap.org/img/wn/13d@2x.png",
    "Shower sleet": "http://openweathermap.org/img/wn/13d@2x.png",
    "Light rain and snow": "http://openweathermap.org/img/wn/13d@2x.png",
    "Rain and snow": "http://openweathermap.org/img/wn/13d@2x.png",
    "Light shower snow": "http://openweathermap.org/img/wn/13d@2x.png",
    "Shower snow": "http://openweathermap.org/img/wn/13d@2x.png",
    "Heavy shower snow": "http://openweathermap.org/img/wn/13d@2x.png",
    # atmosphere
    "mist": "http://openweathermap.org/img/wn/50d@2x.png",
    "Smoke": "http://openweathermap.org/img/wn/50d@2x.png",
    "sand/ dust whirls": "http://openweathermap.org/img/wn/50d@2x.png",
    "Haze": "http://openweathermap.org/img/wn/50d@2x.png",
    "fog": "http://openweathermap.org/img/wn/50d@2x.png",
    "dust": "http://openweathermap.org/img/wn/50d@2x.png",
    "sand": "http://openweathermap.org/img/wn/50d@2x.png",
    "volcanic ash": "http://openweathermap.org/img/wn/50d@2x.png",
    "squalls": "http://openweathermap.org/img/wn/50d@2x.png",
    "tornado": "http://openweathermap.org/img/wn/50d@2x.png",
    # clear
    "clear sky": "http://openweathermap.org/img/wn/01d@2x.png",
    # clouds
    "overcast clouds": "http://openweathermap.org/img/wn/04d@2x.png",
    "broken clouds": "http://openweathermap.org/img/wn/04d@2x.png",
    "scattered clouds": "http://openweathermap.org/img/wn/03d@2x.png",
    "few clouds": "http://openweathermap.org/img/wn/02d@2x.png"
}


@client.command(aliases=["WEATHER", "Weather", "We", "we"])
async def weather(ctx, *, Location):
    api_key = "WEATHER_API_KEY"

    base_url = "http://api.openweathermap.org/data/2.5/weather?appid=784ead9b61bd1b14ffc70bc90e0fe4de&q"

    city_name = Location

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":

        y = x["main"]

        current_temperature = y["temp"]
        temp_centigrade = current_temperature - 273.15
        temp_farenheit = (temp_centigrade * 9 / 5) + 32
        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]

        sentence = weather_description
        words = sentence.split(" ")
        result = ""
        for word in words:
            wethdesc = result + word.capitalize() + " "

        cityname = city_name
        words = cityname.split(" ")
        result = ""
        for word in words:
            capcity = result + word.capitalize() + " "

        embed = discord.Embed(
            colour=discord.Colour.dark_magenta(),
            title=f"Weather in {capcity}",
            description=f"{wethdesc}",
        )
        try:
            icon = Icons[weather_description]
            embed.set_thumbnail(url=icon)
        except KeyError:
            pass

        embed.add_field(name="Temperature", value=f"{round(temp_centigrade)}°C/{round(temp_farenheit)}°F")
        embed.add_field(name="Humidity", value=f"{current_humidity}%")
        embed.add_field(name="Atmospheric Pressure", value=f"{current_pressure}hPa")
        embed.set_footer(text="This System is Powered by openweathermap.org")

        await ctx.send(embed=embed)
    else:

        errorembed = discord.Embed(
            colour=discord.Colour.red(),
            description=f"Location not Found"
        )
        await ctx.send(embed=errorembed)


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

    _8ballembed = discord.Embed(
        colour=discord.Colour.dark_magenta(),
        description=f"{random.choice(responses)}"
    )

    await ctx.send(embed=_8ballembed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    if amount > 200:
        purgembd = discord.Embed(
            colour=discord.Colour.red(),
            title=f"Error!",
            description=f"You cannot purge over 200 messages."
        )
        await ctx.send(embed=purgembd)
#        await asyncio.sleep(10)
    else:
        await ctx.channel.purge(limit=amount + 1)


async def add_cache(self, search, result, t=0, level=1):
    try:
        try:
            if result['error']:
                return
        except KeyError:
            pass
        if t == 0:
            self.image_cache[search] = [result, level]
        elif t == 1:
            self.search_cache[search] = [result, level]
        elif t == 2:
            self.youtube_cache[search] = [result, level]
    except Exception as e:
        print(e)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    kickembed = discord.Embed(
        colour=discord.Colour.red(),
        description=f"{member.mention} has been kicked from the server for {reason}",
        title="Kick"
    )
    await ctx.send(embed=kickembed)


@client.command()
@commands.has_permissions(ban_members=True)
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    banembed = discord.Embed(
        colour=discord.Colour.red(),
        description=f"{member.mention} has been banned from the server for: {reason}",
        title="Ban"
    )
    await ctx.send(embed=banembed)


@client.command()
async def test(ctx):
    testembed = discord.Embed(
        colour=discord.Colour.dark_magenta(),
        description="Bot is running fine!"
    )
    await ctx.send(embed=testembed)


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            unbanembed = discord.Embed(
                colour=discord.Colour.green(),
                title="Unban",
                descripition=f"{user.mention} has been Unbanned from the server"
            )
            await ctx.send(embed=unbanembed)
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
    gayembed = discord.Embed(
        colour=discord.Colour.dark_magenta(),
        title="Ha gayyyyyy",
        description=f"{random.choice(responses)}"
    )
    await ctx.send(embed=gayembed)


@client.command(aliases=["howgay"])
async def gayrate(ctx, *, member):
    responses = random.randint(0, 100)
    rateemebed = discord.Embed(
        colour=discord.Colour.dark_magenta(),
        description=f"{member} is {responses}% gay"
    )
    await ctx.send(embed=rateemebed)


@client.command()
async def spamping(ctx, member: discord.Member, amount: int):
    auth_id = 271366212645027841
    if ctx.message.author.id == auth_id:
        for i in range(amount):
            await ctx.send(member.mention)
            AmountAsInt = int(amount)
            AmountAsInt = AmountAsInt + 1
        await ctx.channel.purge(limit=AmountAsInt)
    else:
        await ctx.send("You do not have access to this command.")


@client.command()
@commands.has_permissions(administrator=True)
async def spam(ctx, text, amount):
    for i in range(int(amount)):
        await ctx.send(f"{text}")
    AmountAsInt = int(amount)
    AmountAsInt = AmountAsInt + 1
    await ctx.channel.purge(limit=AmountAsInt)


# FIX LATER
# @client.command()
# async def join(ctx):
#    author = ctx.message.author
#    channel = author.voice_channel
#    await client.join_voice_channel(channel)

@gay.error
async def gay_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        MRA = discord.Embed(
            colour=discord.Colour.red(),
            description="Please use the format: `.gay {Insert User}`",
            title="Error!"
        )
        await ctx.send(embed=MRA)
    if isinstance(error, commands.MissingPermissions):
        MP = discord.Embed(
            colour=discord.Colour.red(),
            description="You do not have permissions to run this command.",
            title="Error!"
        )
        await ctx.send(embed=MP)


@spamping.error
async def spamping_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please use the format: `.spamping {Insert User}, {Insert Amount of Pings}`")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission to run that command.")


@gayrate.error
async def gayrate_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        MRA = discord.Embed(
            colour=discord.Colour.red(),
            description="Please use the format: `.gayrate {Insert User}` or `.howgay {Insert User}`",
            title="Error!"
        )
        await ctx.send(embed=MRA)
    if isinstance(error, commands.MissingPermissions):
        MP = discord.Embed(
            colour=discord.Colour.red(),
            description="You do not have permissions to run this command.",
            title="Error!"
        )
        await ctx.send(embed=MP)


@weather.error
async def weather_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        MRA = discord.Embed(
            colour=discord.Colour.red(),
            description="Please use the format: `.weather {Insert Location}`",
            title="Error!"
        )
        await ctx.send(embed=MRA)
    if isinstance(error, commands.MissingPermissions):
        MP = discord.Embed(
            colour=discord.Colour.red(),
            description="You do not have permissions to run this command.",
            title="Error!"
        )
        await ctx.send(embed=MP)


@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        MRA = discord.Embed(
            colour=discord.Colour.red(),
            description="Please use the format: `.8ball {Insert Question}`",
            title="Error!"
        )
        await ctx.send(embed=MRA)
    if isinstance(error, commands.MissingPermissions):
        MP = discord.Embed(
            colour=discord.Colour.red(),
            description="You do not have permissions to run this command.",
            title="Error!"
        )
        await ctx.send(embed=MP)


@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        MRA = discord.Embed(
            colour=discord.Colour.red(),
            description=f"Please specify the amount of messages you want to purge",
            title="Error!"
        )
        await ctx.send(embed=MRA)
    if isinstance(error, commands.MissingPermissions):
        MP = discord.Embed(
            colour=discord.Colour.red(),
            description="You do not have permissions to run this command.",
            title="Error!"
        )
        await ctx.send(embed=MP)


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        MRA = discord.Embed(
            colour=discord.Colour.red(),
            description=f"Please specify the user you want to Kick",
            title="Error!"
        )
        await ctx.send(embed=MRA)
    if isinstance(error, commands.MissingPermissions):
        MP = discord.Embed(
            colour=discord.Colour.red(),
            description="You do not have permissions to run this command.",
            title="Error!"
        )
        await ctx.send(embed=MP)


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        MRA = discord.Embed(
            colour=discord.Colour.red(),
            description=f"Please specify the user you want to Ban",
            title="Error!"
        )
        await ctx.send(embed=MRA)
    if isinstance(error, commands.MissingPermissions):
        MP = discord.Embed(
            colour=discord.Colour.red(),
            description="You do not have permissions to run this command.",
            title="Error!"
        )
        await ctx.send(embed=MP)


@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        MRA = discord.Embed(
            colour=discord.Colour.red(),
            description=f"Please specify the user you want to unban",
            title="Error!"
        )
        await ctx.send(embed=MRA)
    if isinstance(error, commands.MissingPermissions):
        MP = discord.Embed(
            colour=discord.Colour.red(),
            description="You do not have permissions to run this command.",
            title="Error!"
        )
        await ctx.send(embed=MP)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print("User tried unexisting Command")


client.run(os.getenv('TOKEN'))