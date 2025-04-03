class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1

        def dp(idx):
            if idx in memo:
                return memo[idx]
            
            if idx < 0:
                return 0
            
            memo[idx] = dp(idx-1) + dp(idx-2)
        
            return memo[idx]
        
        return dp(n)
            
        