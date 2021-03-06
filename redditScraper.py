import os
import praw
import random
from dotenv import load_dotenv

load_dotenv()
REDDIT_BOT_ID = os.getenv('REDDIT_BOT_ID')
REDDIT_BOT_SECRET = os.getenv('REDDIT_BOT_SECRET')
reddit = praw.Reddit(client_id=REDDIT_BOT_ID,
					 client_secret=REDDIT_BOT_SECRET, 
					 user_agent='content_scraper')

def randomRetrive(subreddits ,randomRange=20):
	subreddit = reddit.subreddit(subreddits[random.randint(0,len(subreddits)-1)])
	postlist = []
	for submission in subreddit.top(limit=randomRange):
		nsfw = False
		if not submission.over_18: 
			postlist.append(submission)
		else:
			nsfw = True
	
	if len(postlist) != 0:
		return postlist[random.randint(0, len(postlist)-1)].url
	elif nsfw:
		return "This content is NSFW! No peeking!"