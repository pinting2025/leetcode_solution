class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # dp[1][1] = 1

        # dp[2][1] = 0
        # dp[2][2] = 1

        # dp[3][1] = 1
        # dp[3][2] = 0
        # dp[3][3] = 1

        # dp[4][1] = 1
        # dp[4][2] = 1
        # dp[4][3] = 0
        # dp[4][4] = 1

        dp = [[0 for i in range(j+1)] for j in range(n)]
        dp[0][0] = 1
        
        for i in range(1, n):
            for j in range(1, i+1):
                # forget
                if j >= forget:
                    dp[i][j] = 0
                    continue

                # spread 
                elif j >= delay:
                    dp[i][0] += dp[i-1][j-1]
                
                dp[i][j] = dp[i-1][j-1]
        
        return sum(dp[n-1]) % (10**9+7)

                

        









