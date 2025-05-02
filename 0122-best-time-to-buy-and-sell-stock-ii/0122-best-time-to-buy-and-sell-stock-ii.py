class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # top-down dp
        memo = {}

        def dp(i, flag):
            if (i, flag) in memo:
                return memo[(i, flag)]
            
            if i >= len(prices):
                return 0
            
            if flag == True:
                sell = dp(i+1, flag = False) + prices[i]
                stay = dp(i+1, flag = True)
                memo[(i, flag)] = max(sell, stay)
            
            else:
                buy = dp(i+1, flag = True) - prices[i]
                stay = dp(i+1, flag = False)
                memo[(i, flag)] = max(buy, stay)
            
            return memo[(i, flag)]
    
        return dp(0, flag = False)
    
            

