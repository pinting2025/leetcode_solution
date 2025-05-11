class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(idx, cur):
            if (idx, cur) in memo:
                return memo[(idx, cur)]

            if idx == len(nums):
                return 1 if cur == target else 0
            
            memo[(idx, cur)] = dp(idx+1, cur+nums[idx]) + dp(idx+1, cur-nums[idx])

            return memo[(idx, cur)]
        
        return dp(0, 0)