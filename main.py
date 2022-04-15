# import discord
from BotClient import get_bot
from dotenv import load_dotenv

import os

# intents = discord.Intents(messages=True, guilds=True, typing=True)
bot = get_bot()

def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
