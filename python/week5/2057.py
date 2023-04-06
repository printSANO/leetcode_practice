class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i,j in enumerate(nums):
            if i % 10 == j:
                return i
        return -1