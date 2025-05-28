class Solution:
    def countBits(self, n: int) -> List[int]:
        # top-down
        memo = {}

        def dp(idx):
            if idx in memo:
                return memo[idx]
            
            if idx == 1:
                return 1

            memo[i] = dp(i >> 1) + (i & 1)
            return memo[idx]
        
        res = [0] * (n+1)
        for i in range(1, n+1):
            res[i] = dp(i)

        return res

        # res = [0] * (n + 1)

        # for i in range(1, n+1):
        #     res[i] = res[i//2] + (i & 1)

        # return res