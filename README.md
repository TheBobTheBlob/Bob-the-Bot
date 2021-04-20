# Bob the Bot

A Discord bot written in Python using Discord.py, mostly related to Dungeons and Dragons.
It has some tools to help Game Masters, and also some stuff for fun.
The default prefix is `$`.

## Requirements

* os
* random
* re
* Discord.py

## Features

### Dice Rolls

`$r<Your dice rolls>`

This command uses Python's `random` module to roll the dice. The command accepts several different inputs:

* `<die number>` - Rolls the die once
* `d<die number>` - Rolls the die once (Same as the above command)
* `<number of times to roll>d<die number>` - Rolls the die as many times as specified
* `<number>` - Just a number.
* The bot also has support for parenthesis.
* The above can be linked together with +,-, and *.

### Timetable

If there is a channel dedicated for a timetable the bot will take messages from that and do several things.

* React with the correct reactions so users can easily click instead of searching though the list.

## Other Commands

* `$help`: Shows a help message.
* `$coin`: Flips a coin and shows you the result.
* `$twenty`: Rolls a d20 die with a remarkable chance to get a natural 20.
* `$one`: Just rolls a die with a very high chance of getting a 1. That's it.
