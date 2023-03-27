class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        size1 = r*c
        size2 = len(mat)*len(mat[0])
        if size1 == size2:
            flattened = [j for i in mat for j in i]
            return [[flattened[i+(j*c)] for i in range(c)]for j in range(r)]
        else:
            return mat