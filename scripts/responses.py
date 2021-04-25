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
        result += f"\n{random.choice(nat_20)}"
    elif expression == "d20" and result_data["result"] == 1:
        result += f"\n{random.choice(nat_1)}"

    embed = discord.Embed(
        title=":game_die: Dice Roll Result",
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


def eightball(author, question, result):
    embed = discord.Embed(title=":8ball: Magic 8-Ball", color=embed_colour)
    embed.set_author(name=author.display_name, icon_url=author.avatar_url)
    if len(question) > 0:
        embed.add_field(
            name=":question: Your Question", value=f"{question}", inline=False
        )
        embed.add_field(
            name=":star: My Answer",
            value=f"{result}",
            inline=False,
        )
    else:
        embed.add_field(
            name=":exclamation: No Quesion Asked",
            value="You need to ask me a question so I can use my infinite wisdom and answer it.",
        )
    embed.set_footer(text=f"8-Ball command run by: {author.display_name}")

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
