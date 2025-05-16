class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins = sorted(coins)
        memo = {} 

        def dp(idx, remain):
            if remain == 0:
                return 1
            
            if remain < 0 or idx >= len(coins):
                return 0
            
            if (idx, remain) in memo:
                return memo[(idx, remain)]
            
            skip = dp(idx+1, remain)
            take = dp(idx, remain - coins[idx])

            memo[(idx, remain)] = skip + take

            return memo[(idx, remain)]
        
        return dp(0, amount)