class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculate(i, k):
            if k == 0:
                return 1
            if k == 1:
                return i
            temp = calculate(i, k//2)
            if k % 2 == 0:
                res = temp * temp
            else:
                res = i * temp * temp
            
            return res

        if n < 0:
            return calculate(1/x, -n)

        else:
            return calculate(x, n)

        