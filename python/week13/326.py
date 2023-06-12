class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while True:
            if n == 3 or n == 1:
                return True
            elif n < 3:
                return False
            n = n/3