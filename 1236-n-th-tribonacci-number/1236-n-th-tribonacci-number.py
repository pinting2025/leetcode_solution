class Solution:
    def tribonacci(self, n: int) -> int:
        # bottom-up 
        dp = [0] * 4
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n+1):
            dp[3] = dp[0] + dp[1] + dp[2]
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = dp[3]
        
        return dp[3] if n >= 4 else dp[n]

        # top-down
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1

        def dp(i):
            if i in memo:
                return memo[i]
            
            if i > n:
                return 0
            
            memo[i] = dp(i-1) + dp(i-2) + dp(i-3)

            return memo[i]
        
        return dp(n)


