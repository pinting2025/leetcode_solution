class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom-up
        matrix = [[0 for i in range(n)] for j in range(m)]

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    matrix[r][c] = 1
                else:
                    matrix[r][c] = matrix[r-1][c] + matrix[r][c-1]
    
        return matrix[-1][-1]















        # top-down
        matrix = [[None for i in range(n)] for j in range(m)]
        def dp(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return 0

            if matrix[r][c] != None:
                return matrix[r][c]
            
            if r == 0 or c == 0:
                matrix[r][c] = 1
                return 1
            
            matrix[r][c] = dp(r-1, c) + dp(r, c-1)      

            return matrix[r][c]

        return dp(n, m)