class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        i = 0
        j = 1
        n = len(s)
        while j<= n and i < j:
            ss = s[i:j]
            if len(ss) == len(set(ss)):
                maxLen = max(maxLen, len(ss))
                j += 1
            else:
                i += 1
        return maxLen
            