class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom-up
        dp = [0] * 3
        dp[0] = cost[-1]
        for i in range(len(cost)-1, -1, -1):
            dp[2] = min(dp[0], dp[1]) + cost[i]
            dp[0] = dp[1]
            dp[1] = dp[2]

        return min(dp[0], dp[1])

        # top-down
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            
            if i >= len(cost):
                return 0
            
            one = cost[i] + dp(i+1)
            two = cost[i] + dp(i+2)

            memo[i] = min(one, two)

            return memo[i]
        
        return min(dp(0), dp(1))