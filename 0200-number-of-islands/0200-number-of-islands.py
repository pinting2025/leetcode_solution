class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # check if the current cell is land, if yes, explore by bfs
        queue = deque() # (row, col)
        visited = set()
        res = 0

        def bfs(i, j):
            visited.add((i, j))
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return 
            queue.append((i, j))
            while queue:
                current = queue.popleft()
                if (i-1, j) not in visited:
                    bfs(i-1, j)
                if (i+1, j) not in visited:
                    bfs(i+1, j)
                if (i, j-1) not in visited:
                    bfs(i, j-1)
                if (i, j+1) not in visited:
                    bfs(i, j+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    if (i, j) not in visited:
                        visited.add((i, j))
                        bfs(i, j)
                        res += 1
        
        return res
       

                    