class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
                return 

            else:
                grid[r][c] = '0'
                bfs(r+1, c)
                bfs(r, c+1)
                bfs(r-1, c)
                bfs(r, c-1)

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    res += 1
                    bfs(r, c)
        
        return res

