class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum1 = 0
        sum2 = 0

        for n in range(n+1):
            if n % m == 0:
                sum2 += n
            else:
                sum1 += n
        
        return sum1 - sum2

        