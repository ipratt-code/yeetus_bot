import os
import discord
import keep_alive
from dotenv import load_dotenv
from discord.ext import commands
import itertools
#import random
import redditScraper
#import searchTheWeb

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
prefixes = "'", ";", "??"
bot = commands.Bot(command_prefix=prefixes)
bot.remove_command('help')

#defining helper functions for formatting things nicely etc etc
def listFmt(l):
	fmtStr = ""
	for item in l:
		fmtStr += " " + item + " |"
	return fmtStr[:-1]
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(aliases=['h'], help="Sends this help panel message")
async def help(ctx):
	embed = discord.Embed(color = discord.Color.blue())
	embed.set_author(name="Yeetus_Bot help panel")
	for command in bot.commands:
		embed.add_field(name=listFmt(itertools.chain([command.name], command.aliases)), value=command.help, inline=False)
	await ctx.channel.send(embed=embed)

@bot.command(aliases=['m'], help="Sends a meme from either r/dankmemes or r/memes")
async def meme(ctx):
    await ctx.channel.send(redditScraper.randomRetrive(['dankmemes','memes']))

@bot.command(aliases=['eb'], help="Bleaches your eyes with photos from r/eyebleach and r/aww")
async def eyebleach(ctx):
    await ctx.channel.send(redditScraper.randomRetrive(['eyebleach','aww']))

@bot.command(aliases=['s'], help="Satisfies you with stuff from r/satisfying and r/oddlysatisfying")
async def satisfying(ctx):
	await ctx.channel.send(redditScraper.randomRetrive(['oddlysatisfying','satisfying']))

@bot.command(aliases=['rs'], help="Looks up a subreddit and takes a random top post")
async def redditSearch(ctx, sub):
	try:
		ret = redditScraper.randomRetrive([sub])
	except:
		ret = "Sorry, something went wrong! Try making sure that the subreddit you typed is correct!"
	
	await ctx.channel.send(ret)

keep_alive.keep_alive()
bot.run(TOKEN)