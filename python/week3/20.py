class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        d = {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if i in d:
                lst.append(d[i])
            elif i not in lst or i != lst.pop():
                return False
        if len(lst) == 0:
            return True
        return False