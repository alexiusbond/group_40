# import random as rn
from random import randint as generate_number, choice

import emoji

import calculator

from utils.person import Person

from termcolor import cprint
from decouple import config

print(generate_number(1, 10))
print(calculator.addition(1, 6))

my_friend = Person('Jim', 30)
print(my_friend)

cprint("Hello, World!", "green", "on_red")
print(emoji.emojize('Python is :thumbs_up:'))
print(config('DATABASE_URL'))

commented_var = config('COMMENTED', default=0, cast=int)
print(commented_var * 2)
