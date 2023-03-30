class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            num1 = 9 - board[i].count(".")+1
            num12 = len(set(board[i]))
            num2 = 9 - [board[j][i] for j in range(9)].count(".")+1
            num22 = len(set([board[j][i] for j in range(9)]))
            num3 = 9 - sum([j[(i%3)*3:(i%3)*3+3] for j in board[(i//3)*3:(i//3)*3+3]], []).count(".")+1
            num32 = len(set(sum([j[(i%3)*3:(i%3)*3+3] for j in board[(i//3)*3:(i//3)*3+3]], [])))
            if num1 != num12 or num2 != num22 or num3 != num32:
                return False
        return True
            