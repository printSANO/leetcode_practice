class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        r = 0
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for j in d.values():
            r += sum(range(0,j))
        return r