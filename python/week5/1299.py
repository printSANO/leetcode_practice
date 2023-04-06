class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr += [-1]
        for i in range(len(arr)-2,0,-1):
            arr[i] = max(arr[i], arr[i+1])
        return arr[1:]

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1,1,-1):
            if arr[i-1] < arr[i]:
                arr[i-1] = arr[i]
        arr = arr[1:] + [-1]
        return arr
