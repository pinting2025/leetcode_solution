class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # create power, use bit manupulation
        power = []
        temp = n
        i = 0

        while temp > 0:
            if temp & 1:
                power.append(2**i)

            temp //= 2
            i += 1
        
        # form res
        res = []
        for q in queries:
            start = q[0]
            end = q[1]
            temp = 1
            for i in range(start, end+1):
                temp *= power[i]
            res.append(temp%(10**9+7))
        
        return res


        
        

        