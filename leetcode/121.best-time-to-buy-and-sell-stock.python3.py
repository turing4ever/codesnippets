class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        delta = [prices[i]-prices[i-1] for i in range(1,len(prices))]
        running_sum = max_sum = delta[0]
        for n in delta[1:]:
            running_sum = max(n, running_sum + n)
            max_sum = max(running_sum, max_sum)
        if max_sum > 0:
            return max_sum
        else:
            return 0
