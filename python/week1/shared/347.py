class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = {}
        result = [0]*k
        for i in nums:
            if i in numsDict:
                numsDict[i] += 1
            else:
                numsDict[i] = 1
        sortedVal = sorted(numsDict.items(), key = lambda x:x[1], reverse=True)
        for j in range(k):
            result[j] = sortedVal[j][0]
        return result