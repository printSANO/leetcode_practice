# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        mid = n//2
        pick = guess(mid)
        left = 0
        right = n
        while pick != 0 and left < right:
            if pick < 0:
                right = mid - 1
                mid = (left + right) // 2
                pick = guess(mid)
            else:
                left = mid + 1
                mid = (left + right) // 2
                pick = guess(mid)
        return mid

## this is binary search