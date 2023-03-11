class Solution:
    def longestPalindrome(self, s: str) -> int:
        occurs = {}
        length = 0
        odds = False
        for i in s:
            if i in occurs:
                occurs[i] += 1
            else:
                occurs[i] = 1
        for val in occurs.values():
            if val % 2 == 0:
                length += val
            else:
                odds = True
                if val > 1:
                    length += (val -1)
        if odds:
            length += 1
        return length