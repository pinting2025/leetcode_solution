class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()

        def dfs(i, j):
            nonlocal temp

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 or (i, j) in visited:
                return 
            
            visited.add((i, j))

            if grid[i][j] == 1:
                temp += 1
                dfs(i-1, j)
                dfs(i, j-1)
                dfs(i+1, j)
                dfs(i, j+1)

            return 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    temp = 0
                    dfs(i, j)
                    res = max(res, temp)
        
        return res

            
