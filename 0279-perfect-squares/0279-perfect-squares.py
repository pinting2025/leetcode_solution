class Solution:
    def numSquares(self, n: int) -> int:
        dic = []
        for i in range(1, int(sqrt(n)+1)):
            dic.append(i*i)
        
        memo = {}
        def dp(remain):
            if remain == 0:
                return 0
            
            if remain in memo:
                return memo[remain]

            temp = float('inf')
            for d in dic:
                if d <= remain:
                    temp = min(temp, dp(remain-d) + 1)
                else:
                    break

            memo[remain] = temp
            return memo[remain]

        return dp(n)

            


            

            