class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # bottom-up
        dp = [0] * 3
        dp[0] = nums[-1]
        dp[1] = max(nums[-1], nums[-2])

        for i in range(len(nums)-3, -1, -1):
            dp[2] = max(dp[0]+nums[i], dp[1])
            dp[0] = dp[1]
            dp[1] = dp[2]
        
        return dp[2] if len(nums) > 2 else dp[len(nums)-1]

        # top-down
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            
            if i >= len(nums):
                return 0
            
            rob = dp(i+2) + nums[i]
            skip = dp(i+1)

            memo[i] = max(rob, skip)

            return memo[i]
        
        return dp(0)