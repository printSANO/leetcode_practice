class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        r = 0
        if x < 0:
            return False
        while n != 0:
            digit = n % 10
            r = r * 10 + digit
            n //= 10
        if r == x:
            return True
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        return False