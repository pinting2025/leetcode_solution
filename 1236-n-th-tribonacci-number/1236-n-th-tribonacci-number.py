class Solution:
    def tribonacci(self, n: int) -> int:
        # top-down
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        def dp(idx):
            if idx in memo:
                return memo[idx]
            
            if idx > n or idx < 0:
                return 0
            
            memo[idx] = dp(idx-1) + dp(idx-2) + dp(idx-3)

            return memo[idx]
        
        return dp(n)
        
