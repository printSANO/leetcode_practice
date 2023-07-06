class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        first = 0
        second = 0
        hit_zero = True
        for i in nums:
            if i == 0 and second != 0:
                hit_zero = False
                max_len = max(max_len, first)
                temp = first - second
                first = temp
                second = temp
            elif i == 0 and second == 0:
                hit_zero = False
                second = first
            else:
                first += 1
        max_len = max(max_len, first)
        return max_len - int(hit_zero)