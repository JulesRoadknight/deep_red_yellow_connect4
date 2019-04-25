from random import randint
class Ai():

    def __init__(self, moves):
        self.moves = moves

    def move(self):
        choice = self.select_move()
        while not self.legal(choice):
            choice = self.select_move()
        return choice

    def select_move(self):
        return randint(0,6)

    def legal(self, choice):
        if self.moves.legal_moves[choice] == "Full":
            return False
        return True
