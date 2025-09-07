class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]

        res = []
        if n % 2 == 0:
            pair = n // 2
            for i in range(1, pair+1):
                res.append(i)
                res.append(-i)
        
        else:
            res.append(0)
            pair = (n-1) // 2
            for i in range(1, pair+1):
                res.append(i)
                res.append(-i)
        print(sum(res))
        return res

