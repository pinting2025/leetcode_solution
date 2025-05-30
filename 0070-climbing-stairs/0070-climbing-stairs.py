class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom-up
        dp = [0] * 3
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for _ in range(0, n):
            dp[2] = dp[1] + dp[0]
            dp[0] = dp[1]
            dp[1] = dp[2]

        return dp[2] if n >= 3 else dp[n]

        # top-down 
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2

        def dp(i):
            if i in memo:
                return memo[i]
            
            if i > n:
                return 0
            
            memo[i] = dp(i-1) + dp(i-2)

            return memo[i]
        
        return dp(n)

