class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parent = list(range(n))
        rank = [0] * n
        stack = []

        graph = {}
        for i in range(n):
            graph[i] = []

        def find(x):
            visited = set()
            stack = [x]
            path = []
            
            while stack:
                node = stack[-1]

                if node in visited:
                    stack.pop()
                    continue
                
                visited.add(node)
                path.append(node)

                if parent[node] == node:
                    for p in path:
                        parent[p] = node
                    return node
                
                stack.append(parent[node])
        
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2:
                return 1
            
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            
            return

        for e in edges:
            union(e[0], e[1])
        
        cost = {}
        for e in edges:
            root = find(e[0])
            if root in cost:
                cost[root] &= e[2]
            else:
                cost[root] = e[2]

        res = []
        for q in query:
            if find(q[0]) == find(q[1]):
                res.append(cost[find(q[0])])
            else:
                res.append(-1)
        
        return res











                        


        