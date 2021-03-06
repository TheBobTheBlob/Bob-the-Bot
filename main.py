"""This is the python file that is run to start the bot

Most of the code here is getting inputs ready and sending them
to the correct module, then sending the output to Discord.
"""

import os
import re

import discord

from scripts import responses
from scripts import random_cmds
from scripts import help_cmds


prefix = "$"

activity = discord.Activity(name=f"{prefix}help", type=discord.ActivityType.listening)
client = discord.Client(activity=activity)


@client.event
async def on_message(message):

    # Checks if the message was sent by a bot
    if message.author.bot:
        return

    content = message.content.strip().lower()

    # 758904123784691715 is id for #timetable channel
    if message.channel.id == 758904123784691715:
        reactions = ["✅", "❎"]
        for reaction in reactions:
            await message.add_reaction(reaction)

    # Checks if message starts with prefix
    if not message.content.startswith(prefix):
        return

    # Removes prefix
    content = content[1:]

    # help command
    if content.startswith("help"):
        if content == "help":
            await message.channel.send(embed=help_cmds.bot(message.author, prefix))
        else:
            content = content.split()
            if len(content) == 2:
                await message.channel.send(
                    embed=help_cmds.command(content[1], message.author, prefix)
                )

    # roll command
    elif content.startswith("r"):
        # Removes "roll", "r" and any spaces
        expression = re.sub("(\\s|(roll)|[r])", "", content)

        # If just a number, changes it into a a dice
        if expression.isdecimal():
            expression = "d" + expression
        expression = expression.replace("dice", "d").replace("binay", "b")

        result_data = random_cmds.roll(expression)
        roll_response = responses.roll(message.author, expression, result_data)
        await message.channel.send(embed=roll_response)

    # coin command
    elif content == "coin":
        result, art = random_cmds.coin()
        await message.channel.send(embed=responses.coin(message.author, result, art))

    # 8ball command
    elif content.startswith("8ball"):
        question = " ".join(message.content.strip().split()[1:])
        result = random_cmds.eightball()
        await message.channel.send(
            embed=responses.eightball(message.author, question, result)
        )

    # info command
    elif content == "info" or content == "information":
        await message.channel.send(embed=responses.info(client, message.author))

    # twenty command
    elif content == "twenty":
        await message.channel.send(responses.twenty())

    # one command
    elif content == "one":
        await message.channel.send(responses.one())


client.run(os.environ.get("TOKEN"))
