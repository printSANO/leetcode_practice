class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        l = [sum([1 for j in nums if j%i==0]) for i in divisors]
        m = max(l)
        divisors = [divisors[i] for i in range(len(divisors)) if l[i] == m]
        return min(divisors)