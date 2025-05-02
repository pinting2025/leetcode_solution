class Solution:
    def climbStairs(self, n: int) -> int:
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

