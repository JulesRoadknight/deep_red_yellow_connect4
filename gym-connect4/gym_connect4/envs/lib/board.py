import move

class Board():

    def __init__(self):
        self.game_board = [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]]
        self.moves = move.Move()
    def show(self):
        return self.game_board

    def make_move(self, player, legal_move_index):
        coords = self.moves.save_move(player, legal_move_index)
        self.game_board[coords[1]][coords[0]] = player
