class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        r = []
        d = [0]*(max(nums)+1)
        for i in range(len(nums)):
            if d[nums[i]] == 1:
                r.append(nums[i])
            else:
                d[nums[i]] += 1
        return r