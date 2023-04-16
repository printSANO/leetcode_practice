class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer =""
        for i in range(len(indices)):
            answer += s[indices.index(i)]
        return answer

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = dict(zip(indices,s))
        r = ""
        for i in range(len(d)):
            r += d[i]
        return r