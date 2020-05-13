import discord
from discord.ext import commands
from random import randint

PREFIX              = "/"
BOT_MESSAGE_INIT    = "bot ready"
BOT_MESSAGE_ERROR   = "Wrong Command"
ROLL_COMMAND        = "r"

client = commands.Bot(command_prefix = PREFIX )

@client.event
async def on_ready():
    print(BOT_MESSAGE_INIT)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send(BOT_MESSAGE_ERROR)

@client.command(name = ROLL_COMMAND)
async def roll(ctx, exp, mod = 0):
        number, dice, mod = [exp[0], exp[2:], mod]    
        number  = int(number)
        dice    = int(dice)
        await ctx.send(roll(dice, number, mod))

def roll(dice, number, mod=0):
    roll = 0
    for i in range(1, number+1):
        roll += randint(1,dice)
    
    if mod != 0:
        output = roll + int(mod)
        return f'({roll} + {mod}) = {output}'
    else:
        output = roll
        return f'({output} + 0) = {output}'

client.run("NzA5NDAwNzY0MDc4MDk2NDA3.XrlYuA.9YypSwD9pv0uXocoIB16JcYbpiM")
