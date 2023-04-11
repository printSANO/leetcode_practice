class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        t = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return t
            else:
                t += 1
        return t