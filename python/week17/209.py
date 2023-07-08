class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = 10**5 + 1
        n = len(nums)
        left = 0
        right = 0
        temp_sum = nums[0]
        while left < n and right < n and left <= right:
            if temp_sum == target:
                min_len = min(min_len, right-left+1)
                temp_sum -= nums[left]
                left += 1
            elif temp_sum < target:
                right += 1
                if right == n:
                    break
                temp_sum += nums[right]
            else:
                min_len = min(min_len, right-left+1)
                temp_sum -= nums[left]
                left += 1
        if min_len > 10**5:
            return 0
        return min_len