class Solution:
    def maxArea(self, height: List[int]) -> int:
        x1, x2 = 0, len(height)-1
        maxArea = 0
        while x1 != x2:
            currentArea = (x2-x1) * min(height[x1],height[x2])
            maxArea = max(currentArea, maxArea)
            if height[x1] < height[x2]:
                x1 += 1
            else:
                x2 -= 1
        return maxArea