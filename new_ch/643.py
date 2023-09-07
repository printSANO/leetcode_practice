class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[:k])
        temp = ans
        if len(nums) == 0:
            return ans
        for i in range(len(nums)-k):
            temp -= nums[i]
            temp += nums[k+i]
            ans = max(ans, temp)
        return ans/k
        