#version 1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
          if nums[i] == target:
            return i
        else:
            return -1

# version 2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            val = nums.index(target)
            return val
        except:
            return -1