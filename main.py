import os
import discord
import keep_alive
from dotenv import load_dotenv
from discord.ext import commands
import itertools
import redditScraper
import yaml

with open (r'config.yml') as f:
	config = yaml.load(f, Loader=yaml.FullLoader)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
prefixes = "'", ";", "??"
bot = commands.Bot(command_prefix=prefixes)
bot.remove_command('help')

embedColor = discord.Colour.blue()

#defining helper functions for formatting things nicely etc etc
def listFmt(l):
	fmtStr = ""
	for item in l:
		fmtStr += item + " | "
	return fmtStr[:-2]

async def isDev(ctx):
	for id in config['bot_devs_ids']:
		if ctx.author.id == id:
			return True

@bot.event
async def on_ready():
	print(f'{bot.user} has connected to Discord!')
	await bot.change_presence(activity=discord.Game(name=config["game_status"]))

@bot.command(aliases=['a'], help="DEVS ONLY: send an anouncement to all servers this bot is in")
@commands.check(isDev)
async def announcement(ctx):
	await ctx.channel.send("owo its owner-chan!")

@bot.command(aliases=['st'], help="Changes the status of the bot")
async def status(ctx, *status_tuple):
	status = ""
	for item in status_tuple:
		status += item + " "
	status = status.strip()
	await bot.change_presence(activity=discord.Game(name=status))
	await ctx.channel.send("Changed the status of the bot to `Playing " + status + "`")
	config["game_status"] = status
	with open('config.yml','w') as f:
		yaml.dump(config, f)


@bot.command(aliases=['h', 'he'], help="Sends this help panel message")
async def help(ctx):
	embed = discord.Embed(color = embedColor)
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

@bot.command(aliases=['sa'], help="Satisfies you with stuff from r/satisfying and r/oddlysatisfying")
async def satisfying(ctx):
	await ctx.channel.send(redditScraper.randomRetrive(['oddlysatisfying','satisfying']))

@bot.command(aliases=['rs'], help="Looks up a subreddit and takes a random top post")
async def redditsearch(ctx, sub):
	try:
		ret = redditScraper.randomRetrive([sub])
	except:
		ret = "Sorry, something went wrong! Try making sure that the subreddit you typed is correct!"
	
	await ctx.channel.send(ret)

keep_alive.keep_alive()
bot.run(TOKEN)