class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0:
            return 0

        max_profit = 0
        min_elm = prices[0]

        for i in range(1,len(prices)):
            max_profit = max(max_profit, max(0, prices[i] - min_elm))        
            min_elm = min(min_elm, prices[i])

        return max_profit