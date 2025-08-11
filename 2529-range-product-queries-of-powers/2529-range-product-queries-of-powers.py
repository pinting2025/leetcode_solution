class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        exp = []
        temp = n
        i = 0
        while temp > 0:
            if temp & 1:
                exp.append(i)
            temp //= 2
            i += 1
        
        prefix = [0]
        for e in exp:
            prefix.append(prefix[-1] + e)
        
        res = []
        for l, r in queries:
            t = prefix[r+1] - prefix[l]
            res.append(2**t % (10**9+7))
        
        return res

