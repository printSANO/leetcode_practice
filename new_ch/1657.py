class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1 = Counter(word1)
        d2 = Counter(word2)
        return sorted(d1.values()) == sorted(d2.values()) and d1.keys()==d2.keys()
        