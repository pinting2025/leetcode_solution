class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
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


                

                