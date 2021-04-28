# Bob the Bot

A Discord bot written in Python. It's mostly related to D&D and other roleplaying games but also has some other stuff for fun.

The default prefix is `$`.

## Requirements

* os
* random
* re
* discord.py

## Dice Rolls

`$roll <dice roll expression>` or `$r <dice roll expression>`

This command uses Python's `random` module to roll the dice. It has support for the following inputs:

* `<number>` - If only a number is inputted the bot takes it as a singular roll, if part of an larger expresion it's considered as a normal number.
* `<number of times to roll>d<die number>` - Rolls the die as many times as specified. The number of times can be left blank to roll only once.
* `binary` or `b` - Returns a binary value: 0 or 1

The above can be linked to form an expression using:

* Addition (+), subtraction (-), multiplication (*), and division (/)
* Brackets (): They work in the same way brackets work in maths
* Repeating brackets []: `<number>[<expression>]` It repeats the inner expression as many times as given

## Timetable

A decicated timetable channel can be set up and the bot will do the following:

* React with ✅ and ❎ so users can easily click them instead of searching though the list.

## Other Commands

* `$help`: Shows a help message.
* `$coin`: Flips a coin and shows you the result.
* `$8ball`: Ask a Magic 8-Ball your question and get an answer.
* `$info`: Shows information about the bot.
* `$twenty`: Rolls a d20 die with a remarkable chance to get a natural 20.
* `$one`: Just rolls a die with a very high chance of getting a 1. That's it.
