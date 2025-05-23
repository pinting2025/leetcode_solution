class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # bottom-up
        dp = triangle[-1]
        print(dp)

        for r in range(len(triangle)-2, -1, -1):
            for i in range(len(triangle[r])):
                dp[i] = triangle[r][i] + min(dp[i], dp[i+1])

        return dp[0]

        # # top-down
        # memo = {}

        # def dp(idx, row):
        #     if (idx, row) in memo:
        #         return memo[(idx, row)]
            
        #     if row >= len(triangle) or idx >= len(triangle[row]):
        #         return 0
            
        #     memo[(idx, row)] = min(dp(idx+1, row+1), dp(idx, row+1)) + triangle[row][idx]

        #     return memo[(idx, row)]
        
        # return dp(0,0)

