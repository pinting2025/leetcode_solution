class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # row = len(grid)
        # col = len(grid[0])
        # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        
        # def bfs(target, counted):
        #     queue = deque([(0,0)])
        #     counted = counted
        #     visited = counted.copy()
        #     count = 0

        #     while queue:
        #         r, c = queue.popleft()
        #         if (r,c) not in counted:
        #             if grid[r][c] < target:
        #                 counted.add((r,c))
        #                 count += 1
        #                 # explore four direction
        #                 for mr, mc in direction:
        #                     new_r = r + mr
        #                     new_c = c + mc
        #                     if 0 <= new_r < row and 0 <= new_c < col and ((new_r, new_c) not in visited):
        #                         visited.add((new_r, new_c))
        #                         queue.append((new_r, new_c))

        #     return count, counted
        
        # queries = sorted(queries)
        # res = []
        # counted = set([])
        # count, counted = bfs(queries[0], counted)
        # res.append(count)
        # print(count, counted)
        # count, counted = bfs(queries[1], counted)
        # print(count, counted)

        # # for q in range(1, len(queries)):
        # #     if queries[q-1] == queries[q]:
        # #         res.append(res[-1])
        # #     else:
        # #         count, counted = bfs(queries[q], counted_set)
        # #         print(count, counted)
        # #         res.append(res[-1] + count)
        
        # return res

        n = len(queries)
        rows, cols = len(grid), len(grid[0])
        k_idx, uniq_query = 0, sorted(set(queries))
        
        # BFS preparation
        cache = {}
        visited = {(0, 0)}
        bfs = [(grid[0][0], 0, 0)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        curr = 0
        while bfs and k_idx < len(uniq_query):
            val, r, c = heapq.heappop(bfs)
            
            # If current cell's value >= current query value, update cache
            while k_idx < len(uniq_query) and uniq_query[k_idx] <= val:
                cache[uniq_query[k_idx]] = curr
                k_idx += 1
            
            curr += 1  
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(bfs, (grid[nr][nc], nr, nc))
        
        # Map back to original query order, use .get for query that has higher val than max(grid)
        return [cache.get(queries[i], curr) for i in range(n)]

                   


            










