import board
class Connect4():

    def __init__(self):
        self.game_board = board.Board()

    def start(self):
        player = 2
        not_over = True
        turn = 1
        while not_over and turn <= 42 :
            if player == 1 :
                player = 2
            else:
                player = 1
            self.move(player)
            self.show_board()
            not_over = not self.gameover()
            turn += 1
        if not_over == True:
            print("It's a Draw!")
        else:
            print(f'Player {player} wins')

    def show_board(self):
        return self.game_board.show()

    def gameover(self):
        return self.game_board.moves.check_win()


    def move(self, player):
        player_choice = int(input("Make your move"))
        if player_choice > 7 or player_choice < 1:
            print("Please enter a number from 1-7")
            self.move(player)
        else:
            self.game_board.make_move(player, player_choice-1)
# comment for commit
