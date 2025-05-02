class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        matrix = [[-1 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        
        def dp(i, j):
            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i

            if matrix[i][j] != -1:
                return matrix[i][j]
            
            if word1[i] == word2[j]:
                matrix[i][j] = dp(i+1, j+1)
            else:
                insert = 1 + dp(i, j+1)
                delete = 1 + dp(i+1, j)
                replace = 1 + dp(i+1, j+1)

                matrix[i][j] = min(insert, delete, replace)

            return matrix[i][j]

        return dp(0, 0)