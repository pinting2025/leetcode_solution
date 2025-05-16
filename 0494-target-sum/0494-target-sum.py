class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} # (idx, cur)

        def dp(idx, cur):
            if idx == len(nums):
                return 1 if cur == target else 0
            
            if (idx, cur) in memo:
                return memo[(idx, cur)]
            
            memo[(idx, cur)] = dp(idx + 1, cur + nums[idx]) + dp(idx + 1, cur - nums[idx])

            return memo[(idx, cur)]
        
        return dp(0, 0)


