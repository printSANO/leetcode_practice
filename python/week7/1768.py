class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = max(len(word1), len(word2))
        r = ""
        for i in range(n):
            if i < len(word1):
                r+= word1[i]
            if i < len(word2):
                r+= word2[i]
        return r