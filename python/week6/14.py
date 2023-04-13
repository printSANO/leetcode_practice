class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        ans = ""
        long = strs[0]
        short = strs[-1]
        small = min(long, short)
        for i in range(len(small)):
            if short[i] != long[i]:
                return ans
            ans += small[i]
        return ans