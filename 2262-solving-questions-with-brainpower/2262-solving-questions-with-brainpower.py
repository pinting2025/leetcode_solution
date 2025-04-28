class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
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