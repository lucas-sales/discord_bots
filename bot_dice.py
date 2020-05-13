import discord
from discord.ext import commands
from random import randint
client = commands.Bot(command_prefix = "/" )

@client.event
async def on_ready():
    print("bot ready!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("wrong command!")


@client.command(name = "r")
async def roll(ctx, exp, mod = 0):

        number, dice, mod = [exp[0], exp[2:], mod]    
        number  = int(number)
        dice    = int(dice)
        await ctx.send(d20(dice, number, mod))

def d20(dice, number, mod=0):
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
