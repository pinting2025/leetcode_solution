class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def connect(i, j):
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                if root_i < root_j:
                    parent[root_j] = root_i
                else:
                    parent[root_i] = root_j
            
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected)):
                if isConnected[i][j] == 1:
                    connect(i, j)
        
        res = [find(i) for i in parent]

        return len(set(res))



        