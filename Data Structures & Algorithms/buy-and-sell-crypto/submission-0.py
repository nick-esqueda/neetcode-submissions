class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        if you found the lowest, then there's no need to move L anymore
        if you found another lowest, then obviously there's an opportunity
        """

        if len(prices) == 1:
            return 0

        l = 0
        r = 1
        profit = 0
        while r < len(prices):
            currProfit = prices[r] - prices[l] 
            profit = max(profit, currProfit)

            if prices[r] <= prices[l]:
                l = r
            r += 1
        
        return profit