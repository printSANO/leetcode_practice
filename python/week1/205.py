class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        temp_dict = {}
        for i in range(len(s)):
            if s[i] not in temp_dict:
                if t[i] not in temp_dict.values():
                    temp_dict[s[i]] = t[i]
                else:
                    return False
            elif s[i] in temp_dict:
                if temp_dict[s[i]] == t[i]:
                    pass
                else:
                    return False
        return True