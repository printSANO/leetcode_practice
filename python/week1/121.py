class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        val = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < val:
                val = prices[i]
            current_profit = prices[i] - val
            profit = max(profit, current_profit)
        return profit