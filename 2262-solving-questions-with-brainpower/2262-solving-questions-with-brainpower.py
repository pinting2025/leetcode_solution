class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # bottom-up
        dp = [0] * (len(questions) + 1)

        for i in range(len(questions)-1, -1, -1):
            p, nextq = questions[i]

            skip = dp[i+1]

            if i + nextq + 1 < len(questions):
                take = dp[i + nextq + 1] + p
            else:
                take = p
            
            dp[i] = max(take, skip)
        
        return dp[0]

        # top-down
        memo = {}

        def dp(idx):
            if idx in memo:
                return memo[idx]
            
            if idx >= len(questions):
                return 0
            
            # skip
            skip = dp(idx+1)

            # solve 
            solve = questions[idx][0] + dp(idx+questions[idx][1]+1) 

            memo[idx] = max(skip, solve)

            return memo[idx]
        
        return dp(0)