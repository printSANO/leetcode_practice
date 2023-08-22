class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        ans = ""
        if len(str1) < len(str2):
            shorter = str1
        else:
            shorter = str2
        for i in range(1,len(shorter)+1):
            n = len(shorter)-i+1
            ans = str1[:n]
            ans2 = str2[:n]
            if str1.count(ans) == len(str1)/n and str2.count(ans2) == len(str2)/n:
                return ans
