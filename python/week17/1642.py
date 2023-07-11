import heapq
from typing import List
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        lst = []

        for i in range(1, n):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                heapq.heappush(lst, diff)
            if len(lst) > ladders:
                bricks -= heapq.heappop(lst)
            if bricks < 0:
                return i - 1
        return n - 1
