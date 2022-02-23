from game import Game
from utils import int_input
from art import *
import random


class GuessGame(Game):

    def __init__(self, difficulty: int):
        self.difficulty = difficulty
        self.secret_key = random.randint(1, difficulty)
        self.difficulty_from_user = None

    def generate_secret_key(self):
        self.secret_key = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        self.difficulty_from_user = int_input(f"choose a number between 1 - {self.difficulty}:", None)

    def compare_results(self):
        try:
            if self.secret_key == + self.difficulty_from_user:
                return True
            else:
                return False
        finally:
            pass

    def reset_game(self):
        self.secret_key = random.randint(1, self.difficulty)
        self.difficulty_from_user = None

    def play(self):
        self.get_guess_from_user()
        print(text2art(str(self.compare_results())))
