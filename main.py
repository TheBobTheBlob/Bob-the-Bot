import os

import discord

from scripts import responses
from scripts import dice


prefix = "$"
client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.strip().lower()

    # 261302296103747584 is the code for Avrae
    if message.author.id == 261302296103747584 and "d20" in content:
        if content.endswith(" 1"):
            await message.channel.send(responses.nat_1_response())
        elif content.endswith(" 20"):
            await message.channel.send(responses.nat_20_response())

    # Code for rolling dice
    if content.startswith(prefix + "r"):
        result, count = dice.roll(content[2:].replace(" ", ""))
        roll_response = responses.roll(content[2:], result, count)
        await message.channel.send(f"{message.author.mention}" + roll_response)

    if content.startswith(prefix + "party"):
        pass

    if content == prefix + "twenty":
        await message.channel.send(responses.twenty())


client.run(os.environ.get("TOKEN"))
