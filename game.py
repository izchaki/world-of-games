from utils import int_input, bool_input
import os


class Game:
    def print_properties(self):
        attrs = vars(self)
        print('the properties of this class are:')
        print(', '.join("%s: %s" % item for item in attrs.items()))

    def print_methodes(self):
        methodes = dir(self)
        custome_methodes = []
        for methode in methodes:
            if methode[0] != '_' and type(getattr(self, methode)) == type(self.print_methodes):
                custome_methodes.append(methode)
        print(custome_methodes)

    def start_Game(self):
        try:
            self.play()
        finally:
            self.end_of_game()

    def end_of_game(self):
        answer = bool_input('do you want to play again? y/n:', None)
        os.system('cls||clear')
        if answer:
            self.reset_game()
            self.play()