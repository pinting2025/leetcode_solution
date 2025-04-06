class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        res = []
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i] ,1 + dp[j])

        k = max(dp)
        for i in range(n-1,-1,-1):
            if dp[i] == k:
                res.append(nums[i])
                cur = i
                for j in range(i-1,-1,-1):
                    if res[-1] % nums[j] == 0 and dp[j] == dp[cur] - 1:
                        res.append(nums[j])
                        cur = j
                break
        return res