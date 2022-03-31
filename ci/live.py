from ci.CurrencyRouletteGame import CurrencyRouletteGame
from ci.utils import int_input, bool_input
from ci.GuessGame import GuessGame
from ci.MemoryGame import MemoryGame
import os


def welcome(name):
    return f"Hello {name} and welcome to the World Of Games (WoG).Here you\n can find many cool games to play.\n"


def load_game():
    print(
        f"Please choose a game to play:\n     1  Memory Game - a sequence of numbers  will appear for 1 second and "
        f"you have to guess it\n        back\n     2  Guess Game -guess a number and see if you chose like the "
        f"computer\n     3  Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
    )
    game_id = int_input("Pleas enter witch game do you want to play (enter the game id):", lambda num: 0 < num < 4)
    print('Please choose game difficulty from 1 to 5:')
    difficulty = int_input(
        "Please enter a number that represent the difficult you want to play with(choose between 1-5):",
        lambda num: 0 < num < 6)
    os.system('cls||clear')

    if game_id == 1:
        game = MemoryGame(difficulty)
    elif game_id == 2:
        game = GuessGame(difficulty)
    else:
        game = CurrencyRouletteGame(difficulty)

    game.start_Game()
    answer = bool_input('Do you want to play a different game? y/n:', None)
    if answer:
        load_game()
