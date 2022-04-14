from client import BotClient

import discord
from dotenv import load_dotenv

import signal
import os
import sys

intents = discord.Intents(messages=True, guilds=True, typing=True)
client = BotClient(os.getenv('DISCORD_GUILD'), intents)

# Figure out how to handle awaits in signal handlers
# async def signal_handler(sig, frame):
#     sys.exit(0)

def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    # signal.signal(signal.SIGINT, signal_handler)
    client.run(TOKEN)

if __name__ == '__main__':
    main()
