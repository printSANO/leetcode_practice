class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[0 for i in range(3)] for j in range(3)]
        
        for i, (x,y) in enumerate(moves):
            if i % 2 == 0:
                board[x][y] = 1 #O B
            else:
                board[x][y] = 4 #X A
        
        for i in board:
            if sum(i) == 12:
                return "B"
            elif sum(i) == 3:
                return "A"
        
        for i in zip(*board):
            if sum(i) == 12:
                return "B"
            elif sum(i) == 3:
                return "A"
            
        
        d1 = board[0][0] + board[1][1] + board[2][2]
        d2 = board[0][2] + board[1][1] + board[2][0]

        if d1 == 12 or d2 == 12:
            return "B"
        elif d1 == 3 or d2 == 3:
            return "A"
        
        return "Draw" if len(moves) == 9 else "Pending"