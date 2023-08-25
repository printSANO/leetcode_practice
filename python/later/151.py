class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        l = [i for i in l if i]
        l.reverse()
        s = " ".join(l)
        return s
        