"""This file is for code related to python's random module.

It hosts the following commands: roll, coin, 8ball
"""

import random
import re

# Code for dice rolls


def roll(expression):
    """Acts as a singular function to call the class Dice

    Args:
        expression (str): the expression with dice rolls

    Returns:
        dict: data about dice rolls
    """
    dice = Dice(expression)
    math_expression, result_data = dice.solve()

    if not math_expression.islower():
        result_data["result"] = eval(math_expression, {"__builtins__": None}, {})
        return result_data


class Dice:
    def __init__(self, expression):
        self.expression = expression
        self.roll = 0
        self.total_roll = 0
        self.data = {"rolls": [], "maximums": 0, "minimums": 0}

    def dice(self, die, minimum_value=1):
        """Rolls the die given. eg. d20, 2d10

        Args:
            die (str): the dice to roll

        Returns:
            dict: data about dice rolls
        """

        self.total_roll = 0
        if die[0] == "d":
            self.roll = random.randint(minimum_value, int(die[1:]))
            self.stats(die[1:])
            self.total_roll = self.roll
        else:
            die = die.split("d")
            for i in range(0, int(die[0])):
                self.roll = random.randint(minimum_value, int(die[1]))
                self.total_roll += self.roll
                self.stats(die[1])

    def solve(self):
        """Converts an expression with dice rolls to a mathematical expression.

        Returns:
            str: mathematical expression
            dict: data about dice rolls
        """

        # Splits string along: +, -, *, /, (, ), [, ]
        exp_list = re.split("(\\+|\\-|\\*|\\/|\\(|\\)|\\[|\\])", self.expression)

        for i in range(0, len(exp_list)):
            if "d" in exp_list[i]:
                self.dice(exp_list[i])
                exp_list[i] = str(self.total_roll)

            elif "b" in exp_list[i]:
                self.dice(exp_list[i].replace("b", "d1"), 0)
                exp_list[i] = f"{self.total_roll}"
            elif exp_list[i] == "[":
                rbrackets = 1
                rexpression = i

                while rbrackets > 0:
                    rexpression += 1
                    if exp_list[rexpression] == "[":
                        rbrackets += 1
                    elif exp_list[rexpression] == "]":
                        rbrackets -= 1
                count = 0

                for _ in range(0, int(exp_list[i - 1])):
                    results = roll("".join(exp_list[i+1:rexpression]))

                    count += int(results["result"])
                    self.data["rolls"].extend(results["rolls"])
                    self.data["maximums"] += results["maximums"]
                    self.data["minimums"] += results["minimums"]

                for ii in range(i - 1, rexpression + 1):
                    exp_list[ii] = ""
                exp_list[i] = str(count)

            # Adds "*" before each "(" except if it's the first character
            elif (
                i != 1
                and exp_list[i] == "("
                and exp_list[i - 1] not in ["+", "-", "*", "/"]
            ):
                exp_list[i] = "*" + exp_list[i]

        math_expression = "".join(exp_list)

        return math_expression, self.data

    def stats(self, die):
        """Checks the roll against the criteria and then formats it for Discord.

        Args:
            die (str): the dice that was rolled
        """
        if self.roll == int(die):
            self.data["maximums"] += 1
            self.data["rolls"].append(f"**{self.roll}**")
        else:
            if self.roll == 1:
                self.data["minimums"] += 1
            self.data["rolls"].append(f"{self.roll}")


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
