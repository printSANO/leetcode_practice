class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = [0]*(max(nums)+1)
        for i in range(len(nums)):
            d[nums[i]] += 1
        r = [i for i in range(len(d)) if d[i] == 2]
        return r