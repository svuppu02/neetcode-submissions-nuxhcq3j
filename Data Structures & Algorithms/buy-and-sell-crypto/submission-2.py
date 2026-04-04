class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0

        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                max_prof = max(max_prof, sell-buy)
        return max_prof


            

        

        