class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        zeroes = nums.count(0)
        if zeroes > 1:
            return result
        elif zeroes == 1:
            pos = nums.index(0)
            res = 1
            for i in range(len(nums)):
                if i != pos:
                    res *= nums[i]
                    result[i] = 0
            result[pos] = res
            return result      
        else:
            res = 1
            for i in range(len(nums)):
                res *= nums[i]
            for i in range(len(nums)):
                result[i] = res//nums[i]
            return result
