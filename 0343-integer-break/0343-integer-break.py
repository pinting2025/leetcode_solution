class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        
        if n == 3:
            return 2
        
        num3 = n // 3
        remain = n - int(num3) * 3

        if remain == 0:
            return 3 ** num3
        if remain == 1:
            return 3 ** (num3-1) * 4

        return 3 ** (num3) * 2

                
                
        
        

        