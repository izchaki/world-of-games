from game import Game
from utils import int_input
from art import *
import time
import random
import os


class MemoryGame(Game):
    def __init__(self, difficulty: int):
        self.difficulty = difficulty
        self.sequence = []
        self.sequence_from_user = []

        self.generate_sequence()

    def generate_sequence(self):
        for i in range(self.difficulty):
            self.sequence.append(random.randint(0, 101))

    def get_list_from_user(self):
        count = self.difficulty
        print(f'Please enter {self.difficulty} numbers:')
        while count > 0:
            count = count - 1
            self.sequence_from_user.append(int_input('', None))

    def is_list_equal(self):
        if str(self.sequence) == str(self.sequence_from_user):
            return True
        else:
            return False

    def reset_game(self):
        self.sequence_from_user = []
        self.sequence = []
        self.generate_sequence()

    def play(self):
        print(text2art(','.join(str(e) for e in self.sequence)))
        time.sleep(2)
        os.system('cls||clear')
        self.get_list_from_user()
        os.system('cls||clear')
        result = str(self.is_list_equal())
        print(text2art(result))
        return result
