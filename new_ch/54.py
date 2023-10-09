class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        n = (bottom + 1) * (right + 1)

        result = [0] * n
        index = 0

        while index < n:
            for i in range(left, right+1):
                result[index] = matrix[top][i]
                index += 1
            top += 1
            for i in range(top, bottom+1):
                result[index] = matrix[i][right]
                index += 1
            right -= 1

            if top <= bottom:
                for i in range(right, left-1, -1):
                    result[index] = matrix[bottom][i]
                    index += 1
                bottom -= 1
            if left <= right:
                for i in range(bottom, top-1, -1):
                    result[index] = matrix[i][left]
                    index += 1
                left += 1
        return result

        return result
        