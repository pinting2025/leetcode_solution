class Solution:
    def rob(self, nums: List[int]) -> int:
        # top-down
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            
            if i >= len(nums):
                return 0
            
            take = nums[i] + dp(i+2)
            skip = dp(i+1)

            memo[i] = max(take, skip)

            return memo[i]
        
        return dp(0)