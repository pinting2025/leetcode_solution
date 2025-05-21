class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        memo = {} # (length)

        def dp(length):
            if length in memo:
                return memo[length]
            
            cur = 1 if length >= low else 0            
            
            temp = 0
            if length + zero <= high:
                temp += dp(length+zero)
            
            if length + one <= high:
                temp += dp(length+one)
            
            memo[length] = (temp + cur) % (10**9 + 7)

            return memo[length] 
        
        return dp(0) % (10**9 + 7)
