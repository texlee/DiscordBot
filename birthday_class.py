from dataclasses import dataclass
from datetime import date

@dataclass
class Birthday:
    def __init__(self, data: str):
        self.__process_data(data)
    
    def __process_data(self, data: str):
        split_data = data.split(':')
        self.names = split_data[0].split(',')

        date = split_data[1].split('-')
        self.day = date[0]
        self.month = date[1]

    def is_today_birthday(self, day, month):
        if day == self.day and month == self.month:
            return True
        return False
