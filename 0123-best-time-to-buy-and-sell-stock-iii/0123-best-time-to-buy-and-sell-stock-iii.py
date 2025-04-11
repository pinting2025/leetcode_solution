class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, flag, count):
            if (i, flag, count) in memo:
                return memo[(i, flag, count)]
            
            if i >= len(prices) or count <= 0:
                return 0
            
            if flag == 1:
                sell = dp(i+1, 0, count-1) + prices[i]
                keep = dp(i+1, 1, count)
                memo[(i, flag, count)] = max(sell, keep)
            else:
                buy = dp(i+1, 1, count) - prices[i]
                keep = dp(i+1, 0, count)
                memo[(i, flag, count)] = max(buy, keep)

            return memo[(i, flag, count)]
        
        return dp(0, 0, 2)