class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        while num // 10 != 0:
            num = sum(int(i) for i in str(num))
        return num