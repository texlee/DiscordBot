from dataclasses import dataclass
from pathlib import Path

@dataclass
class Food:
    def __init__(self):
        self.restaurants = self.__set_foods()

    def __set_foods(self):
        food_file = Path('foods.txt')
        rval = []
        with open(food_file, 'r') as f:
            for line in f:
                rval.append(line.rstrip().lstrip())
        return rval

    def get_foods(self):
        return self.restaurants

    def get_gluten_free_foods(self):
        return['Flower Child', 'Chipotle', 'Chilis', 'Fuddruckers', 'Tacos (CORN)', \
            'Chic-fil-A', 'Mod Pizza', 'Sweetgreen', 'PF Changs', 'Jersey Mikes', 'Jason\'s Deli', \
            'Sushi']

    def get_vegan_foods(self):
        return ['Dustin vegan fem/soy boi lul']

food = Food()

def get_food() -> Food:
    return food
