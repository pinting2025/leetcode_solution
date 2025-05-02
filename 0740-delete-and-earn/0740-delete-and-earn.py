class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = Counter(nums)
        
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            
            if i > max(dic):
                return 0
            
            delete = dic[i] * i + dp(i+2)
            keep = dp(i+1)
            memo[i] = max(delete, keep)

            return memo[i]
        
        return dp(0)
        

        