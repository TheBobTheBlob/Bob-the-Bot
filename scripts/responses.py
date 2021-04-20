"""This file is for code related to bot responses to events or commands.

Some of them are just pre-written strings, while other are
Discord's embeds.
"""

import random

import discord


embed_colour = 0xFFFFFD

# List of responses for a natural one
nat_1 = [
    "Your luck is scientifically the worst in the world.",
    "The dice gods have deemed you unworthy.",
    "Oh look, it's your IQ.",
    "The next roll should be a 20. Because that's how probability works right?",
    "Yes, blame the dice for your bad luck.",
    "Does it even matter what die you roll? You'll just get ones.",
    "Look! Bad D&D number!",
    "Have any Inspiration laying around?",
    "There, there.",
    "Maybe using a different bot to roll would help.",
    "If don't succeed, try, try, again. Unfortunately in D&D you only get one roll.",
    "Do roll or not to roll?",
    "Name a more iconic duo. D&D and bad luck.",
]

# List of responses for a natural twenty
nat_20 = [
    "There was a one in 7.5 trillion chance of that happening.",
    '"You are already dead." "Nani?"',
    "I hope that was for something important.",
    "The first time you succeded at something.",
    "Look! Good D&D number!",
    "*Claps*",
    "A miracle has just happened!",
    "Hard work leads to sucess. Is rolling a die hard work?",
    "Nice.",
    "Praise RNGesus.",
    "You picked the right bot for rolls.",
    "Now do it again!",
    "Huzzah! A roll of quality!",
]


def nat_1_response():
    """Gets a random string from nat_1 and returns it.

    Returns:
        str: item from nat_1
    """
    return nat_1[random.randint(1, len(nat_1)) - 1]


def nat_20_response():
    """Gets a random string from nat_20 and returns it.

    Returns:
        str: item from nat_20
    """
    return nat_20[random.randint(1, len(nat_20)) - 1]


def help(author, prefix):
    """Returns the embed help message

    Args:
        prefix (str): the prefix for all commands
        author (obj): Discord author object

    Returns:
        obj: an Discord embed object
    """
    embed = discord.Embed(
        title="Bob the Bot | Help",
        description=f"Prefix: `{prefix}`",
        color=embed_colour,
    )

    embed.add_field(
        name=":game_die: Dice",
        value="Rolls a die/dice expression.\n`roll` `r`",
        inline=True,
    )
    embed.add_field(
        name=":coin: Coin Flips",
        value="Flips a coin.\n`coin`",
        inline=True,
    )
    embed.add_field(
        name=":tada: Party",
        value="[WIP] Configure your D&D party.\n`party` then: `create` `delete` `add` `remove` `nick`",
        inline=False,
    )
    embed.add_field(
        name=":joystick: Other",
        value="All other commmands\n`twenty` `one`",
        inline=False,
    )
    embed.add_field(
        name=":gear: Config",
        value="[WIP] Configure Bob the Bot.\n`config` then: `prefix` `timetable` `welcomemsg` `byemsg`",
        inline=False,
    )
    embed.set_footer(text=f"Help command run by: {author.display_name}")

    return embed


def roll(author, expression, result_data):
    """Creates embed with parameters then returns it.

    Args:
        author (obj): Discord author object
        expression (str): the user's dice expression
        result_data (dict): data about dice rolls

    Returns:
        obj: an Discord embed object
    """
    if len(rolls := ", ".join(result_data["rolls"])) > 1024:
        rolls = f"**{result_data['maximums']}** maximum rolls\n**{result_data['minimums']}** minimum rolls"

    result = f"**{result_data['result']}**"

    if expression == "d20" and result_data["result"] == 20:
        result += f"\n{nat_20_response()}"
    elif expression == "d20" and result_data["result"] == 1:
        result += f"\n{nat_1_response()}"

    embed = discord.Embed(
        title=":game_die: Dice Expression Result",
        color=embed_colour,
    )
    embed.set_author(name=author.display_name, icon_url=author.avatar_url)
    embed.add_field(
        name=":star: Result",
        value=f"You got: {result}",
        inline=False,
    )
    embed.add_field(
        name=":1234: Rolls",
        value=rolls,
        inline=False,
    )
    embed.set_footer(text=f"{author.display_name} rolled: {expression}")

    return embed


def coin(author, result, art):
    """Creates embed with parameters then returns it.

    Args:
        author (Discord mention): used to ping a Discord user
        result (str): coin flip result
        art (str): ascii art

    Returns:
        obj: Discord embed object
    """
    embed = discord.Embed(title=":coin: Coin Flip", color=embed_colour)
    embed.set_author(name=author.display_name, icon_url=author.avatar_url)
    embed.add_field(name=":star: Result", value=f"You got: **{result}**\n```{art}```")
    embed.set_footer(text=f"Coin command run by: {author.display_name}")

    return embed


def twenty():
    """Returns the pre-written response.

    Returns:
        str: A response
    """
    return (
        "Woah, you rolled a 20. Hey DM, look they rolled a 20. What do you mean it "
        "was staged? No, this is the most legitimate legit 20 in the history of D&D."
    )


def one():
    """Returns the pre-written response.

    Returns:
        str: A response
    """
    return (
        "What a incompetent member of society you are. Who cheats to roll a natural"
        " 1? If only there was a way for you to sense my disapproval right now."
    )
