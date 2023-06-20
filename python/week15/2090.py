class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        n = len(nums)
        if n/2 <= k:
            return [-1]*n
        dp = [-1]*n
        #first sum
        dp[k] = sum(nums[0:k*2+1])
        for i in range(k+1,n-k):
            dp[i] = dp[i-1] - nums[i-k-1] + nums[i+k]
        for i in range(k,n-k):
            dp[i] = dp[i] // (k*2+1)
        return dp
