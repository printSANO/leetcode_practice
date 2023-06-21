class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 1
        ans = []
        n = len(nums)
        if n < 1:
            return nums
        temp = [nums[0]]
        while i < n:
            if nums[i] != nums[i-1] + 1:
                if len(temp) > 1:
                    ans.append(f"{temp[0]}->{temp[-1]}")
                    temp = [nums[i]]
                elif len(temp) == 1:
                    ans.append(str(temp[0]))
                    temp = [nums[i]]
                else:
                    temp.append(nums[i])
            else:
                temp.append(nums[i])
            i += 1
        if len(temp) > 1:
            ans.append(f"{temp[0]}->{temp[-1]}")
        elif len(temp) == 1:
            ans.append(str(temp[0]))
        return ans
            