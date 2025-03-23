class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        
        mod = 10 ** 9 + 7   

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 2
        dp[2] = 5

        for i in range(3, n+1):
            dp[i] = dp[i-1] * 2 + dp[i-3]

        return dp[n-1] % mod  