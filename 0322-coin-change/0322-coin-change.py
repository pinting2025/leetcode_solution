class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        memo = {}
        def dp(remain):
            if remain in memo:
                return memo[remain]
            
            if remain == 0:
                return 0
            
            i = 0
            temp = float('inf')
            while i < len(coins) and coins[i] <= remain:
                temp = min(temp, dp(remain - coins[i])+1)
                i += 1
            
            memo[remain] = temp

            return temp
        
        if dp(amount) == float('inf'):
            return -1
            
        return dp(amount)
            

            
            

        