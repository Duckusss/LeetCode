class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        buy = prices[0]
        best = 0
        for sell in prices:
            if sell < buy:
                buy = sell
            if sell - buy > best:
                best = sell - buy
        return best
        """
        if len(prices) <= 1:
            return 0
        buy = 0
        sell = 1
        best = prices[sell] - prices[buy]
        n = len(prices)
        while buy < n-1:
            
            # skips the first few values if the next value is less (downhill).
            
            while buy < n-1 and prices[buy] > prices[buy+1]:
                buy += 1
            
            # finds the index of the max value between buy+1 and the end.
            max_index = buy
            for curr in range(buy+1, n):
                if prices[curr] >= prices[max_index]:
                    max_index = curr
            
            # finds the min value between buy + 1 and max index.
            min_index = buy
            for curr in range(buy+1, max_index):
                if prices[curr] < prices[min_index]:
                    min_index = curr
            
            # replaces best with the bigger value.
            if (prices[max_index]-prices[min_index]> best):
                best = prices[max_index]-prices[min_index]
            
            # repeat from the max_index + 1
            buy = max_index + 1
        return best if best > 0 else 0
        """
        # buy always goes to the lowest value
        # sell moves along the entire array once
        # because sell has to always be lower than buy, when it is, set buy to sell
        # compare buy-sell with best value
        # [6,3,4,2,1,5]
