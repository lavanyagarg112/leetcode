class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0
        maxnum = 0
        length = len(prices)
        for i in range(length-1, -1, -1):
            buy = prices[i]
            sell = maxnum
            if sell - buy > profit:
                profit = sell - buy
            maxnum = max(buy, sell)
                

        return profit