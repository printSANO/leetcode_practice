class Solution:
    def isHappy(self, n: int) -> bool:
        repeat = []
        while True:
            nums = list(str(n))
            nums = [int(i)*int(i) for i in nums]
            n = sum(nums)
            if n == 1:
                return True
            if n in repeat:
                return False
            repeat.append(n)