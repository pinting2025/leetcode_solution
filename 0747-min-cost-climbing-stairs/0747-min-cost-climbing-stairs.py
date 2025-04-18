class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top-down
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            
            if i >= len(cost):
                return 0

            memo[i] = cost[i] + min(dp(i+1), dp(i+2))

            return memo[i]
        
        return min(dp(0), dp(1))
        
        # # bottom-up
        # if len(cost) == 2:
        #     return min(cost)

        # dp = [0] * (len(cost)+1)
        # dp[-2] = cost[-1]
        # for i in range(len(cost)-2, -1, -1):
        #     dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        # return min(dp[0], dp[1])


