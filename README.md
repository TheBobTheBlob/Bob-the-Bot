# Bob the Bot

A Discord bot written in Python using Discord.py, mostly related to Dungeons and Dragons.
It has some tools to help Game Masters, and also some stuff for fun.
The default prefix is `$`.

## Requirements

* os
* random
* re
* Discord.py

## Dice Rolls

`$roll <dice roll expression>` or `$r <dice roll expression>`

This command uses Python's `random` module to roll the dice. It has support for the following inputs:

* `<number>` - Can be used as a normal number in a larger expression Note: If only a number is inputted and nothing else, the bot will take it as a singular die roll
* `<number of times to roll>d<die number>` - Rolls the die as many times as specified. It can be left blank to roll the dice once.
* `<binary>` or `b` - Returns a binary value: 0 or 1

The above can be linked to form an expression using:

* Addition (+), subtraction (-), and multiplication (*)
* Brackets (): they work in the same way brackets work in maths

## Timetable

A decicated timetable channel can be set up and the bot will do the following:

* React with ✅ and ❎ so users can easily click them instead of searching though the list.

## Other Commands

* `$help`: Shows a help message.
* `$coin`: Flips a coin and shows you the result.
* `$8ball`: Ask a Magic 8-Ball your question and get an answer.
* `$twenty`: Rolls a d20 die with a remarkable chance to get a natural 20.
* `$one`: Just rolls a die with a very high chance of getting a 1. That's it.
