class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # bottom-up
        matrix = [[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0
                elif i == 0 and j == 0:
                    matrix[i][j] = 1
                elif i == 0:
                    if matrix[i][j-1] == 1:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = 0
                elif j == 0:
                    if matrix[i-1][j] == 1:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = 0
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[-1][-1]

