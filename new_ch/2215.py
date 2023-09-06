class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [[0],[0]]
        
        ans1 = [i for i in nums1 if i not in nums2]
        ans2 = [i for i in nums2 if i not in nums1]
        ans[0] = list(set(ans1))
        ans[1] = list(set(ans2))
        return ans
        