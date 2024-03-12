import discord
import random
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='%', intents=intents)

def gen_emodji():
    emodji = ["ฅ^•ﻌ•^ฅ", "˶ᵔ ᵕ ᵔ˶", "≽^- ˕ -^≼", "•⩊•"]
    return random.choice(emodji)

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 1:
        return "ОРЕЛ"
    else:
        return "РЕШКА"
    
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
