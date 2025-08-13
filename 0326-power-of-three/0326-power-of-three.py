class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        target = 3**19

        return n > 0 and target % n == 0