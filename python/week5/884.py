class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d = Counter(s1.split(" "))+Counter(s2.split(" "))
        return [i for i,j in d.items() if j == 1]
