class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        actual_graph = defaultdict(list)
        graph = defaultdict(list)
        visited = set()
        res = 0

        for i, j in connections:
            graph[i].append(j)
            actual_graph[i].append(j)
            graph[j].append(i)
        
        def dfs(i):
            nonlocal res
            neighbors = graph[i]
            actual_neighbors = set(actual_graph[i])

            for j in neighbors:
                if j not in visited:
                    if j in actual_neighbors:
                        res += 1
                    visited.add(j)
                    dfs(j)
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
        
        return res




