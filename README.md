# Bob the Bot

A Discord bot written in Python using Discord.py, mostly related to Dungeons and Dragons.
It has some tools to help Game Masters, and also some stuff for fun.

## Requirements

* os
* random
* re
* Discord.py
* psycopg2

## Features

### D20 Responses

The bot responds wih a remark if a user rolls either a one or a twenty in a d20 roll. The responses can be changed by changing `nat_1_responses` and `nat_20_responses` in `dice.py`. This only works if the roll is done using the Discord bot Avrae. This is automatic and requires no commands.

### Dice Rolls

`$r<Your dice rolls>`

This command uses Python's `random` module to roll the dice. The command accepts several different inputs:

* `d<die number>` - Rolls the die once
* `<number of times to roll>d<die number>` - Rolls the die as many times as specified
* `<number>` - Just a number.
* The bot also has support for parenthesis.
* The above can be linked together with +,-, and *.

## Other Commands

* `$twenty` - Rolls a d20 die with a remarkable chance to get a natural 20.
