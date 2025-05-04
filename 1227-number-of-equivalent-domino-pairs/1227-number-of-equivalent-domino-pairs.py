class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = []
        for p in dominoes:
            res.append(sorted(p))
        
        res = sorted(res)
        cur = res[0]
        count = 0
        for p1 in range(len(res)):
            for p2 in range(p1+1, len(res)):
                if res[p1] == res[p2]:
                    count += 1
                else:
                    break
                
        return count

