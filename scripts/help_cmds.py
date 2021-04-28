import discord

from .responses import embed_colour


def bot(author, prefix):
    """Returns the embed help message for the entire bot

    Args:
        prefix (str): the prefix for all commands
        author (obj): Discord author object

    Returns:
        obj: an Discord embed object
    """
    embed = discord.Embed(
        title="Help | Bob the Bot",
        description=f"Prefix: `{prefix}`\nFor more information on a command do `{prefix}help [command]`",
        color=embed_colour,
    )
    embed.add_field(
        name=":game_die: Random",
        value="Commands related to random outputs.\n`roll` `coin` `8ball`",
        inline=False,
    )
    """
    embed.add_field(
        name=":tada: Party",
        value="[WIP] Configure your D&D party.\n`party` then: `create` `delete` `add` `remove` `nick`",
        inline=False,
    )
    """
    embed.add_field(
        name=":joystick: Other",
        value="All other commmands\n`info` `twenty` `one`",
        inline=False,
    )
    """
    embed.add_field(
        name=":gear: Config",
        value="[WIP] Configure Bob the Bot.\n`config` then: `prefix` `timetable` `welcomemsg` `byemsg`",
        inline=False,
    )
    """
    embed.set_footer(text=f"Help command run by: {author.display_name}")

    return embed


def command(command, author, prefix):
    """Returns the embed help message for a specific command

    Args:
        command (str): the command the user entered
        prefix (str): the prefix for all commands
        author (obj): Discord author object

    Returns:
        obj: an Discord embed object
    """
    command_info = {
        "roll": {
            "title": ":game_die: Dice Rolls",
            "description": (
                "Takes a dice expression solves it\n\n**You can have the following in the"
                " expression:**\n• `<number>` - If only a number is inputted the bot takes"
                " it as a singular roll, if part of an larger expresion it's considered as"
                " a normal number.\n• `<number of times to roll>d<die number>` - Rolls the"
                " die as many times as specified. The number of times can be left blank to"
                " roll only once.\n• `binary` or `b` - Returns a binary value: 0 or"
                " 1\n\n**The above can be linked to form an expression using:**\n• Addition (+),"
                " subtraction (-), multiplication (*), and division (/)\n• Brackets (): they work"
                " in the same way brackets work in maths\n• Repeating brackets []: `<number>[<expression>]"
                " It repeats the expression as many times as given"
            ),
            "aliases": ["roll", "r"],
            "variables": " [dice expression]",
        },
        "coin": {
            "title": ":coin: Coin Flip",
            "description": "Flips a coin.",
            "aliases": ["coin"],
            "variables": "",
        },
        "8ball": {
            "title": ":8ball: Magic 8-Ball",
            "description": "Ask the Magic 8-Ball your question.",
            "aliases": ["8ball"],
            "variables": " [question]",
        },
        "info": {
            "title": ":information_source: Information",
            "description": "Gives information about this bot.",
            "aliases": ["info", "information"],
            "variables": "",
        },
    }

    aliases = []
    for command_dict in command_info.values():
        aliases.extend(command_dict["aliases"])

    if command in aliases:
        if command == "r":
            command = "roll"
        embed = discord.Embed(
            title=f"Help | {command_info[command]['title']}",
            description=command_info[command]["description"],
            color=embed_colour,
        )
        embed.add_field(
            name="Usage",
            value=f"`{prefix}{command_info[command]['aliases'][0]}{command_info[command]['variables']}`",
            inline=False,
        )
        aliases = f"`{'` `'.join(command_info[command]['aliases'])}`"
        embed.add_field(name="Aliases", value=aliases, inline=False)
    else:
        embed = discord.Embed(
            title="Help | Unknown Command",
            description="The command you entered does not exist or does not have a help screen",
            color=embed_colour,
        )
    embed.set_footer(text=f"Help command run by: {author.display_name}")

    return embed
