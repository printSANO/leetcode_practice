class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = 0
        if low % 2 == 1:
            n += 1
            low += 1
        if high % 2 == 1:
            n += 1
            high -= 1
        n+= (high-low)//2
        return n