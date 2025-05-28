class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:  
        matrix = [[-1 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]

        def dp(i, j):
            if i >= len(text2) or j >= len(text1):
                return 0

            if matrix[i][j] != -1:
                return matrix[i][j]
            
            if text1[j] == text2[i]:
                temp = dp(i+1, j+1) + 1
            
            else:
                temp = max(dp(i+1, j), dp(i, j+1))
            
            matrix[i][j] = temp
            
            return temp
        
        
        print(matrix)
        
        return dp(0, 0)

            
        # dp = [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
        # for i in range(1, len(text2)+1):
        #     for j in range(1, len(text1)+1):
        #         if text2[i-1] == text1[j-1]:
        #             dp[i][j] = dp[i-1][j-1] + 1

        #         else:
        #             dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        # return dp[-1][-1]
        