class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) <= 1:
            return 0
        buy, sell = -prices[0], 0
        for i in prices[1:]:
            buy = max(buy, sell-i)
            sell = max(sell, i-fee+buy)
        return sell