class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9+7

        dic = []
        i = 1
        while True:
            if i ** x <= n:
                dic.append(i ** x)
            else:
                break
            i += 1
        
        dp = [0] * (n+1)
        dp[0] = 1

        for d in dic:
            for s in range(n, d-1, -1):
                dp[s] = (dp[s] + dp[s-d]) % MOD

        return dp[n]
        
        # # create a list of possible numbers
        # dic = []
        # for i in range(1, int(n**(1/x))+2):
        #     dic.append(i**x)
        
        # memo = {}
        # def dp(idx, remain):
        #     if remain == 0:
        #         return 1
            
        #     if (idx, remain) in memo:
        #         return memo[(idx, remain)]
            
        #     if idx >= len(dic) or remain < 0:
        #         return 0
            
        #     take = dp(idx+1, remain-dic[idx])
        #     skip = dp(idx+1, remain)

        #     memo[(idx, remain)] = (take + skip) % (10**9+7)
        #     return memo[(idx, remain)]
        
        # return dp(0, n)



        
        