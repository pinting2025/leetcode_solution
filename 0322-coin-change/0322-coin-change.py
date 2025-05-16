class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        memo = {} # remain

        def dp(remain):
            if remain == 0:
                return 0
            
            if remain in memo:
                return memo[remain]
            
            temp = float('inf')
            for coin in coins:
                if remain - coin < 0:
                    break
                temp = min(temp, dp(remain-coin) + 1)

            memo[remain] = temp

            return memo[remain]
        
        return dp(amount) if dp(amount) != float('inf') else -1