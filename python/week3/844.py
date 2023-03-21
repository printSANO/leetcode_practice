from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        d1 = deque()
        d2 = deque()
        def stack(deq, strings):
            for i in strings:
                if i == "#":
                    try:
                        deq.pop()
                    except:
                        pass
                else:
                    deq.append(i)
            return deq

        if stack(d1, s) == stack(d2, t):
            return True
        return False