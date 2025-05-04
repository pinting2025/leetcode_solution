class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic = Counter()
        res = 0

        for p in dominoes:
            p = tuple(sorted(p))
            if p in dic:
                res += dic[p]
                dic[p] += 1
            else:
                dic[p] = 1

        return res
            
        


