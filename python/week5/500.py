class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r = []
        d = {"q": 1, "w": 1, "e": 1, "r": 1, "t": 1, "y": 1, "u": 1, "i": 1, "o": 1, "p": 1, "p": 1, "a": 2, "s": 2, "d": 2, "f": 2, "g": 2, "h": 2, "j": 2, "k": 2, "l": 2, "z": 3, "x": 3, "c": 3, "v": 3, "b": 3, "n": 3, "m": 3}
        for k in range(len(words)):
            i = words[k]
            new_i = [d[j] for j in i.lower()]
            length = len(new_i)
            if new_i.count(1) == length or new_i.count(2) == length or new_i.count(3) == length:
                r.append(i)
        return r