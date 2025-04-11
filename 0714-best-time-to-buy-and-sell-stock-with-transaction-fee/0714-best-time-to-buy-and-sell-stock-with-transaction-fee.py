class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}

        def dp(i, flag):
            if (i, flag) in memo:
                return memo[(i, flag)]
            
            if i >= len(prices):
                return 0

            # holding stock 
            if flag == 1:
                sell = dp(i+1, 0) + prices[i] - fee
                keep = dp(i+1, 1)
                memo[(i, flag)] = max(sell, keep)
            
            # not holding
            else:
                buy = dp(i+1, 1) - prices[i]
                keep = dp(i+1, 0)
                memo[(i, flag)] = max(buy, keep)

            return memo[(i, flag)]
        
        return dp(0,0)
            
            


             


