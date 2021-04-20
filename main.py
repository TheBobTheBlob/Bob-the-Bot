"""This is the python file that is run to start the bot

Most of the code here is getting inputs ready and sending them
to the correct module, then sending the output to Discord.
"""

import os
import re

import discord

from scripts import responses
from scripts import dice
from scripts import coin

prefix = "$"
client = discord.Client()


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
    if content == "help":
        await message.channel.send(embed=responses.help(message.author, prefix))

    # roll command
    elif content.startswith("r"):
        # Removes "roll", "r" and any spaces
        expression = re.sub("(\\s|(roll)|[r])", "", content)

        if content.isdecimal():
            expression = "d" + expression

        result_data = dice.roll(expression)
        roll_response = responses.roll(message.author, expression, result_data)
        await message.channel.send(embed=roll_response)

    elif content == "coin":
        result, art = coin.flip()
        await message.channel.send(embed=responses.coin(message.author, result, art))

    # twenty command
    elif content == "twenty":
        await message.channel.send(responses.twenty())

    # one command
    elif content == "one":
        await message.channel.send(responses.one())


client.run(os.environ.get("TOKEN"))
