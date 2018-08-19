class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        delta = [prices[i]-prices[i-1] for i in range(1, len(prices))]
        profit = 0
        for n in delta:
            if n > 0:
                profit += n
        return profit
        
