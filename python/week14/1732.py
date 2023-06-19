class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        temp = 0
        max_height = 0
        for i in gain:
            temp += i
            max_height = max(temp, max_height)
        return max_height