class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # top-down
        memo = {}

        def dp(row, idx):
            if (row, idx) in memo:
                return memo[(row, idx)]
            
            if row >= len(matrix):
                return 0
            
            if idx < 0 or idx >= len(matrix[row]):
                return 0
            
            right = dp(row, idx+1)
            down = dp(row+1, idx)
            dr = dp(row+1, idx+1)
            
            if int(matrix[row][idx]) == 0:
                memo[(row, idx)] = 0
            else:
                memo[(row, idx)] = int(matrix[row][idx]) + min(right, down, dr)

            return memo[(row, idx)]
        
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res = max(res, dp(i, j))

        return res ** 2