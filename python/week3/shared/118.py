class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [[1]*i for i in range(1,numRows+1)]
        if numRows < 3:
            return lst
        else:
            for i in range(2, numRows):
                for j in range(1,i):
                    lst[i][j] = lst[i-1][j-1] + lst[i-1][j]
        return lst