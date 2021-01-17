"""
This file is for code related to bot responses to events or commands.

These responses are not calculated from any data or variables.
They are pre-written and stored in lists or strings.
"""

import random

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
    "If don't succeed, Try, try, again. Unfortunately in D&D you only get one roll.",
]

nat_20 = [
    "There was a one in 7.5 trillion chance of that happening.",
    '"You are already dead."\n"Nani?"',
    "I hope that was for something important.",
    "The first time you succeded at something.",
    "Look! Good D&D number!",
    "*Claps*",
    "A miracle has just happened!",
    "Hard work leads to sucess. Is rolling a die hard work?",
    "Nice.",
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


def twenty():
    """Returns the pre-written response.

    Returns:
        str: A response
    """
    return (
        "Woah, you rolled a 20. Hey DM, look they rolled a 20. What do you mean it "
        "was staged? No, this is the most legitimate legit 20 in the history of D&D."
    )


def roll(expression, result, count):
    """Creates reply with parameters then returns it.

    Args:
        expression (str): the user's dice expression
        result (int): result of the expression
        count (list): data about dice rolls

    Returns:
        str: response for the bot to send
    """
    lenght = 0
    for roll in count[0]:
        lenght += len(roll.strip("**"))

        if lenght > 1000:
            break

    if lenght > 1000:
        response = (
            f"\n**You rolled:** {expression}\n**Rolls:** You got {count[1]} maximum rolls"
            f" and {count[2]} minimum rolls\n**Total:** {result}"
        )
    else:
        rolls = ", ".join(count[0])
        response = (
            f"\n**You rolled:** {expression}\n**Rolls:** {rolls}"
            f"\n**Total:** {result}"
        )
    return response
