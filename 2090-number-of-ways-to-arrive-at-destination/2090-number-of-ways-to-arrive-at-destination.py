class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7
        weight = {}
        neighbours = defaultdict(list)
        min_cost = [float(inf) for i in range(n)]
        count = Counter()
        count[0] = 1
        for road in roads:
            a, b, w = road
            weight[(a, b)] = w
            weight[(b, a)] = w
            neighbours[a].append(b)
            neighbours[b].append(a)
        
        heap = [(0, 0)] # cost, to_node
        while heap:
            cost, node = heapq.heappop(heap)
            if cost > min_cost[node]:
                continue
                
            for neigh in neighbours[node]:
                new_cost = cost + weight[(node, neigh)]
                if new_cost < min_cost[neigh]:
                    min_cost[neigh] = new_cost
                    count[neigh] = count[node] % mod
                    heapq.heappush(heap, (new_cost, neigh))
                elif new_cost == min_cost[neigh]:
                    count[neigh] += count[node] % mod
        return count[n - 1] % mod            
