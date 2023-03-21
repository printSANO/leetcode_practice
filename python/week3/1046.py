class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = stones
        while len(s) > 1:
            s = sorted(s, reverse=True)
            f1 = s.pop(0)
            if f1 == s[0]:
                s.pop(0)
            else:
                s[0] = f1-s[0]
        return 0 if len(s) == 0 else s[0]