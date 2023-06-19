class Solution:
    def findComplement(self, num: int) -> int:
        n = bin(num).replace("0b", "")
        n = ['0' if i == '1' else '1' for i in n]
        n = "".join(n)
        return int(n,2)