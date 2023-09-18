class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        print(nums)
        ans = 0
        a = 0
        b = len(nums) - 1
        while a < b:
            n = nums[a] + nums[b]
            if n < k:
                a += 1
            elif n > k:
                b -= 1
            else:
                ans += 1
                a += 1
                b -= 1
        return ans