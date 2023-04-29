class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s += s
        if len(s)/2 != len(goal):
            return False
        return goal in s