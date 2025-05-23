class Solution:
    def numSquares(self, n: int) -> int:
        memo = {} # remain

        dic = []
        for i in range(1, 101):
            dic.append(i**2)

        def dp(remain):
            if remain == 0:
                return 0

            if remain in memo:
                return memo[remain]
            
            temp = float('inf')
            for i in dic:
                if remain - i >= 0:
                    temp = min(temp, dp(remain-i) + 1)
                else:
                    break
                
            memo[remain] = temp

            return memo[remain]

        return dp(n)
                

        
        