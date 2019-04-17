import board
class Connect4():

    def __init__(self):
        self.game_board = board.Board()

    def start(self):
        player = 2
        not_over = True
        while not_over :
            if player == 1 :
                player = 2
            else:
                player = 1
            self.move(player,input("Make your move")-1)
            self.show_board()
            not_over = not self.gameover()
        print(f'Player {player} wins')

    def show_board(self):
        return self.game_board.show()

    def gameover(self):
        return self.game_board.moves.check_win()


    def move(self, player, legal_move_index):
        self.game_board.make_move(player, legal_move_index)
# comment for commit
