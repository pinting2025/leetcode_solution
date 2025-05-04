class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}

        def dp(row, idx):
            if (row, idx) in memo:
                return memo[(row, idx)]
            
            if row == len(matrix):
                return 0
            
            if idx < 0 or idx >= len(matrix):
                return float('inf')
            
            left = dp(row+1, idx-1)
            right = dp(row+1, idx+1)

            memo[(row, idx)] = matrix[row][idx] + min(left, right, dp(row+1, idx))

            return memo[(row, idx)]
        
        res = float('inf')
        for i in range(len(matrix[0])):
            res = min(res, dp(0, i))

        return res
