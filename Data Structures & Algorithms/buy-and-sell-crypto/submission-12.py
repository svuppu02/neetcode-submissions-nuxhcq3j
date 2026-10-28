class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxP = max(profit, maxP)
            else:
                buy = sell
            sell += 1
            

        return maxP

        








