class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]

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

        for l1, l2 in zip(s1, s2):
            i = ord(l1) - ord('a')
            j = ord(l2) - ord('a')

            connect(i, j)

        res = []
        for l in baseStr:
            i = ord(l) - ord('a')
            res.append(chr(find(i) + ord('a')))
        
        return "".join(res)