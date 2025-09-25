class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        def dp(idx, cur_row):
            if (idx, cur_row) in memo:
                return memo[(idx, cur_row)]

            if idx > cur_row:
                return float('inf')
            
            if cur_row >= len(triangle):
                return 0
            
            memo[(idx, cur_row)] = min(dp(idx, cur_row+1)+triangle[cur_row][idx], dp(idx+1, cur_row+1)+triangle[cur_row][idx])

            return memo[(idx, cur_row)]
        
        return dp(0, 0)

            
        
