# based on https://realpython.com/how-to-make-a-discord-bot-python/

import os
import discord


def calculatefibonacci(first_number, second_number, size_of_output):
    output = [first_number, second_number]
    while output.__len__() != size_of_output:
        third_number = first_number + second_number
        output.append(third_number)
        first_number = second_number
        second_number = third_number

    return output


client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        print("connected to guild %s" % guild)


@client.event
async def on_message(message):
    if message.author == client.user:
        return  # ignore messages sent by the bot

    words = message.content.split(" ")
    if(words.__len__() > 0):
        if words[0] == '!fibo':
            first_number = 1
            second_number = 1
            size_of_output = 5
            if words.__len__() > 1:
                first_number = int(words[1])
            if words.__len__() > 2:
                second_number = int(words[2])
            if words.__len__() > 3:
                size_of_output = int(words[3])

            if size_of_output < 3:
                await message.channel.send("third parameter must be 3 or more")
            elif size_of_output > 1000:
                await message.channel.send("that is excessive")
            else:
                try:
                    fibo_results = calculatefibonacci(first_number, second_number, size_of_output)
                    number_of_messages_sent = 0
                    for guild in client.guilds:
                        for member in guild.members:
                            if client.user != member: # dont sent this to the bot to bot
                                await member.create_dm()  # creates a DM channel to the member
                                await member.dm_channel.send(
                                    f'Hi {member.name}, here is a fibonnaci sequence! {fibo_results}'
                                )
                                number_of_messages_sent = number_of_messages_sent + 1

                    # tell the author how many people received the message:
                    result = "%s was sent to %s members" % (fibo_results, number_of_messages_sent)
                    await message.channel.send(result)
                    print(result)
                except discord.errors.HTTPException as e:
                    await message.channel.send("failed to send messages: %s" % e)


client.run(os.getenv('DISCORD_TOKEN'))
