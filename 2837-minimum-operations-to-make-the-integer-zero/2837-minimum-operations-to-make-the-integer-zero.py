class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(0, 61):
            temp = num1 - (i*num2)
            cur = temp.bit_count()
            if cur <= i <= temp:
                return i
        
        return -1