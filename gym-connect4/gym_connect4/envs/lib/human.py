class Human():

    def __init__(self, moves):
        self.moves = moves

    def move(self):
        choice = int(input("Make your move Human: "))
        while not self.legal(choice):
            choice = int(input("Please make a legal move: "))
        return choice -1

    def legal(self, choice):
        if choice < 1 or choice > 7 or self.moves.legal_moves[choice -1] == "Full":
            return False
        return True
