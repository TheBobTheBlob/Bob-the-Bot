"""This file is for code related to python's random module.

It hosts the following commands: roll, coin, 8ball
"""

import random
import re

# Code for dice rolls


def roll(expression):
    """Converts a expression with dice rolls into a signle number.

    Args:
        expression (str): the expression with dice rolls

    Returns:
        dict: data about dice rolls
    """
    math_expression, result_data = solve_rolls(expression)

    if not math_expression.isalpha():
        result_data["result"] = eval(math_expression)
        return result_data


def dice(die):
    """Rolls the die given. eg. d20, 2d10

    Args:
        die (str): the dice to roll

    Returns:
        dict: data about dice rolls
    """

    result_data = {"result": 0, "rolls": [], "maximums": 0, "minimums": 0}

    if die[0] == "d":
        result_data["result"] = random.randint(1, int(die[1:]))
        result_data = roll_stats(die[1:], result_data)
    else:
        die = die.split("d")
        for i in range(0, int(die[0])):
            result_data["result"] = random.randint(1, int(die[1]))
            result_data = roll_stats(die[1:], result_data)

    return result_data


def solve_rolls(expression):
    """Converts an expression with dice rolls to a mathematical expression.

    Args:
        expression (str): the expression with dice rolls

    Returns:
        str: mathematical expression
        dict: data about dice rolls
    """

    result_data = {"result": 0, "rolls": [], "maximums": 0, "minimums": 0}

    # Splits string along: +, -, *, (, )
    string_list = re.split("(\\+|\\-|\\*|\\(|\\))", expression)

    for i in range(0, len(string_list)):
        if "d" in string_list[i]:
            old_result_data = dice(string_list[i])
            string_list[i] = str(old_result_data["result"])
            result_data["rolls"].extend(old_result_data["rolls"])
            result_data["maximums"] += old_result_data["maximums"]
            result_data["minimums"] += old_result_data["minimums"]

        # Adds "*" before each "("
        if string_list[i] == "(" and string_list[i - 1][-1:].isdigit():
            string_list[i] = "*" + string_list[i]

    expression = "".join(string_list)

    return expression, result_data


def roll_stats(die, result_data):
    """Checks the roll against the criteria and then formats it for Discord.

    Args:
        die (str): the dice that was rolled
        result_data (dict): data about dice rolls

    Returns:
        dict: data about dice rolls
    """
    if result_data["result"] == int(die):
        result_data["maximums"] += 1
        result_data["rolls"].append(f"**{result_data['result']}**")
    else:
        if result_data["result"] == 1:
            result_data["minimums"] += 1
        result_data["rolls"].append(f"{result_data['result']}")

    return result_data


# Code for coin flips

heads = """
  ▄▄█▀▀▀▀▀█▄▄
▄█▀         ▀█▄
█    █   █    █
█    █▀▀▀█    █
█    █   █    █
▀█▄         ▄█▀
  ▀▀█▄▄▄▄▄█▀▀
"""

tails = """
  ▄▄█▀▀▀▀▀█▄▄
▄█▀         ▀█▄
█   ▀▀▀█▀▀▀   █
█      █      █
█      █      █
▀█▄         ▄█▀
  ▀▀█▄▄▄▄▄█▀▀
"""


def coin():
    """Flips a coin.

    Returns:
        str: result of coin flip
        str: ascii art
    """
    coin = random.randint(1, 2)
    if coin == 1:
        return "Heads.", heads
    else:
        return "Tails.", tails


# Code for 8-ball

eightball_responses = [
    "As I see it, yes.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don’t count on it.",
    "It is certain.",
    "It is decidedly so.",
    "Most likely.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Outlook good.",
    "Reply hazy, try again.",
    "Signs point to yes.",
    "Very doubtful.",
    "Without a doubt.",
    "Yes.",
    "Yes – definitely.",
    "You may rely on it.",
]


def eightball():
    return random.choice(eightball_responses)
