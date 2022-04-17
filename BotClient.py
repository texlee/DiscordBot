from food import get_food
from birthday_class import is_birthday
from locks import get_file_lock
from reddit import get_reddit
from meme import meme_of_the_day
from jokeapi import Jokes

from discord.ext.commands import Bot, Context, CommandNotFound
from discord import Intents, Message

from asyncio import sleep
from threading import Lock
import datetime
import random

# intents_input = Intents(members=True, dm_messages=True, guild_messages=True, guild_reactions=True, guilds=True, messages=True, typing=True)
intents_input = Intents().all()
bot = Bot(command_prefix='?', intents=intents_input)

@bot.event
async def on_command_error(ctx: Context, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@bot.event
async def on_ready():
    bot.loop.create_task(is_birthday(bot))
    bot.loop.create_task(meme_of_the_day(bot, get_reddit()))

@bot.before_invoke
async def write_command_call_to_file(ctx: Context):
    lock: Lock = get_file_lock()
    lock.acquire()
    with open('command_calls.txt', 'a') as f:
        f.write(f'{ctx.author.display_name} executed command: {ctx.invoked_with} at {datetime.datetime.today()}\n')
    lock.release()

@bot.command()
async def food(ctx: Context, arg = None):
    food = get_food()
    if '-g' == arg:
        restaurant = random.choice(food.get_gluten_free_foods())
    elif '-v' == arg:
        restaurant = random.choice(food.get_vegan_foods())
    else:
        restaurant = random.choice(food.get_foods())
    await ctx.send(f'Feeling up for {restaurant}, {str(ctx.author).split("#")[0]}?')

@bot.command()
async def joke(ctx: Context):
    jokes = await Jokes()
    joke = await jokes.get_joke(blacklist=['racist'])
    # joke = await jokes.get_joke(category=['dark'], blacklist=['nsfw', 'religious', 'political', 'racist'])
    if joke["type"] == "single": # Print the joke
        await ctx.send(f'{joke["joke"]}')
    else:
        await ctx.send(f'{joke["setup"]}')
        await sleep(3)
        await ctx.send(f'{joke["delivery"]}')


def get_bot():
    return bot
