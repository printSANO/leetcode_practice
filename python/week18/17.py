class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6':['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        ans = []
        if not digits:
            return []
        
        def helper(comb, num):
            if not num:
                ans.append(comb)
                return
            for letter in d[num[0]]:
                helper(comb + letter, num[1:])
        helper('', digits)
        return ans