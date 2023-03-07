class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums = [0]+nums
        for i in range(1, len(nums)-1):
            if sum(nums[0:i]) == sum(nums[i+1:len(nums)+1]):
                return i-1
        if sum(nums[2:]) == 0:
            return 0
        elif sum(nums[:-1]) == 0:
            return len(nums) - 2
        return -1