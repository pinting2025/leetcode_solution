class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows = len(moveTime)
        cols = len(moveTime[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        heap = [[0, 0, 0]]
        visited = set()
        while heap:
            curr = heapq.heappop(heap)
            t, r, c= curr
            if r == rows - 1 and c == cols - 1:
                return t

            if (r,c) in visited:
                continue
            visited.add((r,c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                if (nr, nc) in visited:
                    continue
                
                wait = max(0, moveTime[nr][nc] - t)
                nt = t + wait + 1
                heapq.heappush(heap, (nt, nr, nc))
        return -1