class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
            
        while n != 1:
            if int(n/4) == n/4:
                n = n/4
            else:
                return False
        
        return True