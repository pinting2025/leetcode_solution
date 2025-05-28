class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def tree(edges):
            n = len(edges) + 1
            adj = [[] for _ in range(n)]

            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            
            return adj
        
        def dfs(adj, u, p, k):
            if k < 0:
                return 0
            
            count = 1

            for v in adj[u]:
                if v != p:
                    count += dfs(adj, v, u, k-1)
            return count
        
        adj1 = tree(edges1)
        adj2 = tree(edges2)
        temp = 0

        for i in range(len(adj2)):
            temp = max(temp, dfs(adj2, i, -1, k-1))

        res = []
        for i in range(len(adj1)):
            res.append(dfs(adj1, i, -1, k) + temp)
        
        return res
        