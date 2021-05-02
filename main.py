import discord
import json

from discord.ext import commands

#read config
with open("config.json") as file:
    config = json.load(file)


# constants
TOKEN = config.token
PREFIX = config.prefix
STATUS = "HiddenBot break constantly"

# variables
client = commands.Bot(command_prefix = PREFIX, case_insensitive = True)


# functions


# events
@client.event
async def on_ready():  # when bot is ready
    print("ready!")

    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = STATUS))


# commands
@client.command(description = "debug command", hidden = True)
async def getchannelpositions(ctx):  # debugging
    channels = await ctx.guild.fetch_channels()
    for channel in channels:
        print("%s : %s" % (channel.name, channel.position))


@client.command(description = "Purge X amount of messages from channel")
async def purge(ctx, args=[]):  # purge messages
    num = None

    # invalid amount
    if len(args) == 0:
        await ctx.channel.send(content = "Please specify how many messages to purge.", delete_after = 5.0)
        return
    else:
        num = "".join(args)

        isdigit = num.isdigit()
        if not isdigit:
            await ctx.channel.send(content = "Please specify how many messages to purge.", delete_after = 5.0)
            return
        else:
            num = int(num)

    await ctx.message.delete()
    await ctx.channel.purge(limit = num)

    await ctx.channel.send(content = "Successfully purged %d messages." % num, delete_after = 5.0)

client.run(TOKEN)