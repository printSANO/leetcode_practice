class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums = [str(i) for i in nums]
        nums = "".join(nums).split("0")
        nums = [len(i) for i in nums]
        return max(nums)