class Move():
    def __init__(self):
        self.legal_moves = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]]
        self.player1 = []
        self.player2 = []

    def add_legal_move(self, coords):
        self.legal_moves.insert(coords[0], coords)

    def save_move(self, player, legal_move_index):
        self.player = player
        if player == 1:
            move = self.legal_moves.pop(legal_move_index)
            self.player1.insert(0, move)
            self.legal_moves.insert(legal_move_index, [move[0],move[1]+1])

        else :
            move = self.legal_moves.pop(legal_move_index)
            self.player2.insert(0, move)
            self.legal_moves.insert(legal_move_index, [move[0],move[1]+1])
        return move

    def check_win(self):
        if len(self.player1) > 3 :
            return self.check_vertical() or self.check_horizontal() or self.check_diagonal()
        return False

    def check_vertical(self):
        collum = []
        total = 0
        if self.player == 1:
            for coords in self.player1:
                if coords[1] != 3 : continue
                valid_coord = coords[0]
                for co_ord in self.player1:
                    if valid_coord == co_ord[0] : collum.append(co_ord)
        else :
            for coords in self.player2:
                if coords[1] != 3 : continue
                valid_coord = coords[0]
                for co_ord in self.player2:
                    if valid_coord == co_ord[0] : collum.append(co_ord)
        for coords in collum:
            total += coords[1]

        if total == 6 or total == 10 or total == 14:
            return True
        else:
            return False

    def check_horizontal(self):
        row = []
        if self.player == 1:
            last_move = self.player1[0]
            for coords in self.player1:
                if coords[1] == last_move[1]: row.append(coords)
        else:
            last_move = self.player2[0]
            for coords in self.player2:
                if coords[1] == last_move[1]: row.append(coords)

        if row.count([0,last_move[1]]) == 1 and row.count([1,last_move[1]]) == 1 and row.count([2,last_move[1]]) == 1 and row.count([3,last_move[1]]) == 1:
            return True
        if row.count([1,last_move[1]]) == 1 and row.count([2,last_move[1]]) == 1 and row.count([3,last_move[1]]) == 1 and row.count([4,last_move[1]]) == 1:
            return True
        if row.count([2,last_move[1]]) == 1 and row.count([3,last_move[1]]) == 1 and row.count([4,last_move[1]]) == 1 and row.count([5,last_move[1]]) == 1:
            return True
        if row.count([3,last_move[1]]) == 1 and row.count([4,last_move[1]]) == 1 and row.count([5,last_move[1]]) == 1 and row.count([6,last_move[1]]) == 1:
            return True
        return False

    def check_diagonal(self):

        if self.player == 1:
            last_move = self.player1[0]
            moves_to_check = self.player1
        else:
            last_move = self.player2[0]
            moves_to_check = self.player2

        if moves_to_check.count([last_move[0]-1, last_move[1]-1]) == 1 and moves_to_check.count([last_move[0]-2,last_move[1]-2]) == 1 and moves_to_check.count([last_move[0]-3, last_move[1]-3]) == 1:
            return True
        if moves_to_check.count([last_move[0]-1, last_move[1]-1]) == 1 and moves_to_check.count([last_move[0]-2,last_move[1]-2]) == 1 and moves_to_check.count([last_move[0]+1, last_move[1]+1]) == 1:
            return True
        if moves_to_check.count([last_move[0]-1, last_move[1]-1]) == 1 and moves_to_check.count([last_move[0]+2,last_move[1]+2]) == 1 and moves_to_check.count([last_move[0]+1, last_move[1]+1]) == 1:
            return True
        if moves_to_check.count([last_move[0]+3, last_move[1]+3]) == 1 and moves_to_check.count([last_move[0]+2,last_move[1]+2]) == 1 and moves_to_check.count([last_move[0]+1, last_move[1]+1]) == 1:
            return True
        if moves_to_check.count([last_move[0]+1, last_move[1]-1]) == 1 and moves_to_check.count([last_move[0]+2,last_move[1]-2]) == 1 and moves_to_check.count([last_move[0]+3, last_move[1]-3]) == 1:
            return True
        if moves_to_check.count([last_move[0]+1, last_move[1]-1]) == 1 and moves_to_check.count([last_move[0]+2,last_move[1]-2]) == 1 and moves_to_check.count([last_move[0]-1, last_move[1]+1]) == 1:
            return True
        if moves_to_check.count([last_move[0]+1, last_move[1]-1]) == 1 and moves_to_check.count([last_move[0]-2,last_move[1]+2]) == 1 and moves_to_check.count([last_move[0]-1, last_move[1]+1]) == 1:
            return True
        if moves_to_check.count([last_move[0]-3, last_move[1]+3]) == 1 and moves_to_check.count([last_move[0]-2,last_move[1]+2]) == 1 and moves_to_check.count([last_move[0]-1, last_move[1]+1]) == 1:
            return True
        return False
