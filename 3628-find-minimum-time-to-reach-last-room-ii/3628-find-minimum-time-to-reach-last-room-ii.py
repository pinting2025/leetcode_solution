class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows = len(moveTime)
        cols = len(moveTime[0])
        heap = [(0,0,0,1)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        res = float('inf')
        while heap:
            val, r, c, step = heapq.heappop(heap)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            
            if r == rows - 1 and c == cols - 1:
                return val
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= rows or nc >= cols or nc < 0 or nr < 0:
                    continue
                if (nr, nc) in visited:
                    continue
                if val < moveTime[nr][nc]:
                    time = step + moveTime[nr][nc]
                else:
                    time = step + val
                heapq.heappush(heap, (time, nr, nc, (step % 2) + 1))