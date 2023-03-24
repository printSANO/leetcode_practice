class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxVal = float('-inf')
        tempMax = 0
        for i in range(len(nums)):
            tempMax += nums[i]
            maxVal = max(tempMax, maxVal)
            tempMax = max(tempMax, 0)
        return maxVal