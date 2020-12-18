import os
import discord
import keep_alive
from dotenv import load_dotenv
from discord.ext import commands
#import random
import redditScraper
#import searchTheWeb

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(aliases=['m'])
async def meme(ctx):
    await ctx.channel.send(redditScraper.randomRetrive(['dankmemes','memes']))

@bot.command(aliases=['eb'])
async def eyebleach(ctx):
    await ctx.channel.send(redditScraper.randomRetrive(['eyebleach','aww']))

@bot.command(aliases=['s'])
async def satisfying(ctx):
	await ctx.channel.send(redditScraper.randomRetrive(['oddlysatisfying','satisfying']))

@bot.command(aliases=['rs'])
async def redditSearch(ctx):
	pass
keep_alive.keep_alive()
bot.run(TOKEN)