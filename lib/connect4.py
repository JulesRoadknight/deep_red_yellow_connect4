import board
import move
class Connect4():

    def __init__(self):
        self.game_board = board.Board()
        self.moves = self.game_board.moves

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
            not_over = not self.gameover()
            turn += 1

        if not_over == True:
            print("It's a Draw!")
        else:
            self.show_board()
            print(f'Player {player} wins')

    def show_board(self):
        string = ""
        i = len(self.game_board.game_board)-1
        while i > -1:
            row = self.game_board.game_board[i]
            for token in row:
                string +=  f'|{token}|'
            string += "\n"
            i -= 1
        print(string)

    def gameover(self):
        return self.game_board.moves.check_win()


    def move(self, player):
        self.show_board()
        player_choice = int(input("Make your move: "))
        if player_choice > 7 or player_choice < 1:
                print("Please enter a number from 1-7")
                self.move(player)
        else:
            if self.moves.legal_moves[player_choice-1] == "Full":
                print("That column is full, please choose again.")
                self.move(player)
            else:
                self.game_board.make_move(player, player_choice-1)
