from event_types import CommandType
from birthday_class import Birthday

import discord
from discord.ext.tasks import loop
from discord.ext.commands import Bot, Command
from pathlib import Path
import random
from datetime import date

restaurants = [
    'Pluckers',
    'Chipotle',

]

async def my_test():
    print ('in my_test command')

class BotClient(discord.Client):
    def __init__(self, guild, intents_input: any):
        super(BotClient, self).__init__(intents=intents_input)
        self.guild_token = guild
        self.foods = self.__get_foods()
        self.birthdays: list(Birthday) = self.__get_birthdays()
        command_test = Command(my_test)
        Bot.add_command(command=command_test)

    def __get_foods(self):
        food_file = Path('foods.txt')
        rval = []
        with open(food_file, 'r') as f:
            for line in f:
                rval.append(line.rstrip().lstrip())
        return rval

    def __get_birthdays(self):
        food_file = Path('birthdays.txt')
        rval: list(Birthday) = []
        with open(food_file, 'r') as f:
            for line in f:
                bday_data = Birthday(line.lstrip().rstrip())
                rval.append(bday_data)
        return rval

    def __process_message_content(self, msg_content) -> CommandType:
        msg_content_split = msg_content.split(' ')
        command_type = msg_content_split[0]
        if command_type == 'food':
            return CommandType.Food
        elif command_type == 'birthday':
            return CommandType.Birthday

        return CommandType.NoCommandType

    def __is_command(self, msg_content: str) -> bool:
        new_lines_check = msg_content.split('\n')
        if len(msg_content) == 0 or msg_content[0] != '!' or len(new_lines_check) > 1:
            return False
        return True

    async def on_message(self, message: discord.Message):
        if not self.__is_command(message.content) or message.author == self.user:
            return
        print (f'channel id: {message.channel}')
        message.content = str(message.content[1:]).lower() # removes bang operator
        msg_type: CommandType = CommandType.NoCommandType
        try:
            msg_type = self.__process_message_content(message.content)
            if msg_type == CommandType.NoCommandType:
                return
        except Exception as e:
            await message.channel.send('Internal error. Report error to Tex Lee Villarreal for OwO debugging.')

        if msg_type == CommandType.Food:
            await message.channel.send(f'Feeling up for {random.choice(self.foods)}, {message.author.name}?')
        elif msg_type == CommandType.Birthday:
            await message.channel.send('It\'s your birthday!')

    @loop(seconds=10, count=None)
    async def __any_birthdays(self):
        print ('in birthdays test')
        todays_date = str(date.today()).split('-')
        day = todays_date[1]
        month = todays_date[2]
        for birthday in self.birthdays:
            if birthday.is_today_birthday(day, month):
                # self.get_channel()
                print ('today is the birthday')

    async def on_ready(self):
        print ('In on_ready')
        # self.loop.create_task(self.__any_birthdays())
        # self.__any_birthdays().start()

