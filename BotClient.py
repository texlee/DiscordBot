from discord.ext.commands import Bot, Context, CommandNotFound
from food import get_food
from birthday_class import is_birthday

import random

bot = Bot(command_prefix='!')

allowed_commands = ['food']

@bot.event
async def on_command_error(ctx: Context, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@bot.event
async def on_ready():
    bot.loop.create_task(is_birthday(bot))

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

def get_bot():
    return bot
