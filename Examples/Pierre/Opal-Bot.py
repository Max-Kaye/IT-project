import discord
from discord.ext import commands, tasks
import os
import random
import asyncio
from itertools import cycle

from flask import ctx

client = commands.Bot(command_prefix=".")
status = cycle(["My developer is an epic developer", "I am an epic bot"])


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
async def on_member_join(member):
    print(f"{member} has joined a server")


@client.event
async def on_member_remove(member):
    print(f"{member} has left or been removed from a Server")


@client.command()
async def ping(ctx):
    await ctx.send(f"The Ping is at: {round(client.latency * 1000)} ms")


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
async def purge(ctx, amount=10):
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
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return


client.run(os.getenv('TOKEN'))
