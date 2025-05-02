class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # top-down
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return float('inf')
            
            if i == 0 and j == 0:
                memo[(i, j)] = grid[0][0]
            elif i == 0:
                memo[(i, j)] = dp(i, j-1) + grid[i][j]
            elif j == 0:
                memo[(i, j)] = dp(i-1, j) + grid[i][j]
            else:
                memo[(i, j)] = min(dp(i-1, j), dp(i, j-1)) + grid[i][j]

            return memo[(i, j)]
        
        return dp(len(grid)-1, len(grid[0])-1)

        # bottom-up
        matrix = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    matrix[i][j] = grid[i][j]
                elif i == 0:
                    matrix[i][j] = matrix[i][j-1] + grid[i][j]
                elif j == 0:
                    matrix[i][j] = matrix[i-1][j] + grid[i][j]
                else:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1]) + grid[i][j]
        
        return matrix[-1][-1]


                

                