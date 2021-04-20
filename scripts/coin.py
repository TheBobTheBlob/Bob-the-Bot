"""Flips a coin and returns the result.

Using Python's random module, it simulates a coin toss.
It then returns the result as well as some ascii art.
"""

import random

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


def flip():
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
