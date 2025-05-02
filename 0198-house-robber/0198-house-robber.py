class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom-up

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