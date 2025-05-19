class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # top-down
        memo = {}

        def dp(idx):
            if idx in memo:
                return memo[idx]
            
            if idx == len(s):
                return True
            
            for w in wordDict:
                if s[idx:idx+len(w)] == w and dp(idx+len(w)):
                    memo[idx] = True
                    return True

            memo[idx] = False
            return False

        return dp(0)
                
        # # bottom-up
        # dp = [False] * (len(s) + 1)
        # dp[-1] = True

        # for i in range(len(s) - 1, -1, -1):
        #     for w in wordDict:
        #         if i + len(w) <= len(s) and s[i:i+len(w)] == w:
        #             dp[i] = dp[i+len(w)]
        #         if dp[i]:
        #             break
        
        # return dp[0]



            



        