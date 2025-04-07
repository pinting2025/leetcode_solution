class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2

        memo = [[None for _ in range(target+1)] for _ in range(len(nums))]

        def dp(i, cur):
            if cur == target:
                return True
            
            if cur > target or i >= len(nums):
                return False

            if memo[i][cur] is not None:
                return memo[i][cur]
            
            take = dp(i+1, cur+nums[i])
            skip = dp(i+1, cur)

            memo[i][cur] = take or skip

            return memo[i][cur]

        return dp(0, 0)