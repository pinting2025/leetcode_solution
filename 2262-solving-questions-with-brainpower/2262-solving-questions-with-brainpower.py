class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n-1, -1, -1):
            point, nextq = questions[i]

            skip = dp[i+1]

            if i + nextq + 1 < n:
                take = dp[i + nextq + 1] + point
            else:
                take = point
            
            dp[i] = max(take, skip)
        
        return dp[0]


