class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        for i in range(len(s)):
            if i+1 < len(s) and romanDict[s[i]] < romanDict[s[i+1]]:
                num -= int(romanDict[s[i]])
            else:
                num += int(romanDict[s[i]])
        return num