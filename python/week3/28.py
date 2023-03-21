import re
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x = re.search(needle, haystack)
        if x is None:
            return -1
        return x.span()[0]