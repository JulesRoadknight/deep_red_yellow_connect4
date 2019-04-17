import board 
class Connect4():

    def __init__(self):
        self.board = board.Board()

    #     self.playing_board = [["-,-,-,-,-,-,-"],
    #         ["-,-,-,-,-,-,-"],
    #         ["-,-,-,-,-,-,-"],
    #         ["-,-,-,-,-,-,-"],
    #         ["-,-,-,-,-,-,-"],
    #         ["-,-,-,-,-,-,-"],
    #         ["-,-,-,-,-,-,-"]
    # ]

    def show_board(self):
        return self.board.show()

    def start(self):

        print("Player 1 wins")
        return self.playing_board

    def move(self, player, column):
        print('Enter your move: ')
        column = input()
        return True
# comment for commit

