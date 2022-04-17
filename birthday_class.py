from discord.ext.commands import Bot
from discord import Guild, utils, Role

from dataclasses import dataclass
import datetime
from asyncio import sleep
import os

@dataclass
class Birthdays:
    def __init__(self):
        self.birthdays = self.__process_data()
    
    def __process_data(self):
        rval = []
        with open('birthdays.txt', 'r') as f:
            birthdays = f.readlines()
            for birthday in birthdays:
                split_data = birthday.split(':')
                names = split_data[0]

                date = split_data[1].split('-')
                month = str(date[0])
                day = str(date[1])
                rval.append({ 'names': names, 'month': month, 'day': day })
        return rval

    def is_today_birthday(self, month, day) -> str | None:
        for birthday in self.birthdays:
            if month == birthday['month'] and day == birthday['day']:
                return birthday['names']
        return None

async def is_birthday(bot: Bot):
    data = Birthdays()
    while True:
        # sleep until 12PM
        t = datetime.datetime.today()
        future = datetime.datetime(t.year,t.month,t.day,12,0)
        if t.hour >= 12:
            future += datetime.timedelta(days=1)
        await sleep((future-t).total_seconds())
        today = str(datetime.date.today()).split('-')[1:]
        names = data.is_today_birthday(today[0], today[1])
        if names is not None:
            guild: Guild = bot.get_guild(int(os.getenv('DISCORD_GUILD_ID')))
            print (f'Its somebodies birthday: {names}')
            # role: Role = utils.get(guild.roles, name='Everyone Jr')
            # channel_id = int(os.getenv('AYYLMAO_ID'))
            # # Enable mention role
            # await role.edit(mentionable=True)
            # await bot.get_channel(channel_id).send(f'Hey, {role.mention}.  It\'s {names}\'s birthday!! Wish them well! *smile*')
            # # Disable mention role
            # await role.edit(mentionable=False)

    # Old way
    # while True:
    #     today = str(date.today()).split('-')[1:]
    #     names = data.is_today_birthday(today[0], today[1])
    #     if names is not None:
    #         guild: Guild = bot.get_guild(int(os.getenv('DISCORD_GUILD_ID')))
    #         role: Role = utils.get(guild.roles, name='Everyone Jr')
    #         channel_id = int(os.getenv('AYYLMAO_ID'))
    #         # Enable mention role
    #         await role.edit(mentionable=True)
    #         await bot.get_channel(channel_id).send(f'Hey, {role.mention}.  It\'s {names}\'s birthday!! Wish them well! *smile*')
    #         # Disable mention role
    #         await role.edit(mentionable=False)

    #     await sleep(86400) # sleeps for a whole day
