class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {} # (idx)

        def dp(idx):
            if idx >= len(nums):
                return 0
            
            if idx in memo:
                return memo[idx]
            
            temp = 1
            for j in range(idx+1, len(nums)):
                if nums[j] > nums[idx]:
                    temp = max(temp, dp(j) + 1)
            
            memo[idx] = temp
            return memo[idx]
        
        res = 1
        for i in range(len(nums)):
            res = max(res, dp(i))

        return res
            