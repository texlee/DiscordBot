from asyncpraw import Reddit
from discord.ext.commands import Bot

import os
from asyncio import sleep

async def meme_of_the_day(bot: Bot, reddit: Reddit):
    while True:
        subreddit = await reddit.subreddit("meme")
        async for submission in subreddit.top(time_filter="day", limit=1):
            channel_id = int(os.getenv('AYYLMAO_ID'))
            await bot.get_channel(channel_id).send(f'Meme of the day: {submission.shortlink}')
        await sleep(86400) # sleeps for a whole day
