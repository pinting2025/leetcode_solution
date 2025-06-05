class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque() # (row, col)
        time = 1
        total = 0
        visited = set()
        direction = [(-1,0), (0, -1), (0, 1), (1, 0)]
        
        # add rotten oranges into queue
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] != 0:
                    total += 1

        count = len(queue)
        if count == total:
            return 0

        while queue:
            if count == total:
                return time-1

            for _ in range(len(queue)):
                current = queue.popleft()
                if current not in visited:
                    visited.add(current)
                    r, c = current[0], current[1]
                    for dr, dc in direction:
                        if dr+r >= 0 and dr+r < len(grid) and dc+c >= 0 and dc+c < len(grid[0]) and grid[dr+r][dc+c] == 1:
                            grid[dr+r][dc+c] = 2
                            queue.append((dr+r, dc+c))
                            count += 1
            
            time += 1
        
        return -1
            
        

        
