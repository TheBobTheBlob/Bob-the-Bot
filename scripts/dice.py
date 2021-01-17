"""
This file is for code related to rolling dice.

It uses Python's random module to pseudo-randomly get rolls.
It has support for any type of die any number of times. eg. d20, 2d10
Also has support for addition, subtraction, muliplication, and parentheses.
"""

import random
import re


def roll_stats(die, roll, count):
    """Checks the roll against the criteria and then formats it for Discord.

    Args:
        die (str): the dice to roll
        roll (int): what the die rolled
        count (int): previous number of maximum and mimimum rolls

    Returns:
        int: the result formatted for Discord
        list: number of maximum and minimum rolls
    """
    if roll == int(die):
        count[0] += 1
    if roll == 1:
        count[1] += 1

    if roll == int(die):
        roll = "**" + str(roll) + "**"
    else:
        roll = str(roll)
    return roll, count


def dice(die):
    """Rolls the die given. eg. d20, 2d10

    Args:
        die (str): the dice to roll

    Returns:
        str: result from dice rolls
        list: data about dice rolls
    """
    result = 0
    rolls = []
    count = [0, 0]

    if die[0] == "d":
        result = random.randint(1, int(die[1:]))
        roll, count = roll_stats(die[1:], result, count)
        rolls.append(roll)
    else:
        die = die.split("d")
        for i in range(0, int(die[0])):
            roll = random.randint(1, int(die[1]))
            result += roll
            roll, count = roll_stats(die[1], roll, count)
            rolls.append(roll)

    return str(result), [rolls, count]


def solve_rolls(expression):
    """Converts an expression with dice rolls to a mathematical expression.

    Args:
        expression (str): the expression with dice rolls

    Returns:
        str: mathematical expression
        list: data about dice rolls
    """

    count = [[], 0, 0]

    string_list = re.split("(\\+|\\-|\\*|\\(|\\))", expression)

    for i in range(0, len(string_list)):
        if "d" in string_list[i]:
            string_list[i], old_count = dice(string_list[i])
            count[0].extend(old_count[0])
            count[1] += old_count[1][0]
            count[2] += old_count[1][1]
        if string_list[i] == "(" and string_list[i - 1][-1:].isdigit():
            string_list[i] = "*" + string_list[i]

    expression = "".join(string_list)

    return expression, count


def roll(expression):
    """Converts a expression with dice rolls into a signle number.

    Args:
        expression (str): the expression with dice rolls

    Returns:
        int: solution to expression as one number
        list: data about dice rolls
    """
    math_expression, count = solve_rolls(expression)

    if not math_expression.isalpha():
        return eval(math_expression), count
