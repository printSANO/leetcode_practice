class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = set([i for i in range(1, len(nums)+1)])
        return list(ans - set(nums))
