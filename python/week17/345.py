class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        locs = []
        rev_vows = []
        for i in range(len(s)):
            if s[i] in vowels:
                locs.append(i)
                rev_vows.append(s[i])
        rev_vows.reverse()
        for j in range(len(locs)):
            s[locs[j]] = rev_vows[j]
        return ''.join(s)
