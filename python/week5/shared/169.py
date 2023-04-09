class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)
        sd = sorted(d.items(), reverse=True, key = lambda x:x[1] )
        return sd[0][0]