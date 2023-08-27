class Solution:
    def compress(self, chars: List[str]) -> int:
        h = ""
        s = ""
        num = 0
        for i in range(len(chars)):
            if h != chars[i]:
                s += h
                if num != 0:
                    s += str(num+1)
                h = chars[i]
                num = 0
            elif h == chars[i]:
                num += 1
        s += h
        if num != 0:
            s += str(num+1)
        for i in range(len(s)):
           chars[i] = s[i]
        l = len(chars) - len(s)
        if l > 0:
            for j in range(l):
                chars.pop(i+1)