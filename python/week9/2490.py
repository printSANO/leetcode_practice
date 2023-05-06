class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        l = sentence.split(' ')
        l1 = [i[0] for i in l]
        l2 = [i[-1] for i in l]
        if len(l) > 1:
            l2 = l2[-1:] + l2[:-1]
        return l1==l2