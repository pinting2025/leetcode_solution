class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        len_r = len(matrix)
        len_c = len(matrix[0])
        memo = {}
        def dp(r, c):
            key = (r, c)
            # look for past result
            if key in memo:
                return memo[key]
            
            # base case
            if r >= len_r:
                return 0
            
            if c >= len_c or c < 0:
                return 999999999

            left = dp(r+1, c-1) + matrix[r][c]
            down = dp(r+1, c) + matrix[r][c]
            right = dp(r+1, c+1) + matrix[r][c]

            res = min(left, down, right)
            memo[key] = res

            return res
        
        res = float('inf')
        for i in range(len_r):
            res = min(res, dp(0, i))
        
        return res
        

            

        