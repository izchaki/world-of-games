from currency_converter import CurrencyConverter
from game import Game
from utils import int_input
from art import *
import random

c = CurrencyConverter()


class CurrencyRouletteGame(Game):

    def __init__(self, d: int):
        self.d = d
        self.mony_in_dolars = random.randint(1, 100)
        self.t = c.convert(self.mony_in_dolars, 'USD', 'ILS')
        self.guess_from_user = None
        self.money_interval = (self.t - d, self.t + d)

    def get_money_interval(self):
        self.money_interval = (self.t - self.d, self.t + self.d)

    def get_guess_from_user(self):
        print(f"Please guess how much {self.mony_in_dolars}$ is worth in shekels? :")
        self.guess_from_user = int_input(f"Please guess how much {self.mony_in_dolars}$ is worth in shekels? :", None)

    def reset_game(self):
        self.mony_in_dolars = random.randint(1, 100)
        self.t = c.convert(self.mony_in_dolars, 'USD', 'ILS')
        self.guess_from_user = None
        self.money_interval = (self.t - self.d, self.t + self.d)

    def play(self):
        self.get_guess_from_user()
        mini, maxi = self.money_interval

        if mini < self.guess_from_user < maxi:
            print(text2art('True'))
        else:
            print(text2art('False'))
