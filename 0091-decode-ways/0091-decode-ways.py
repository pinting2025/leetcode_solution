class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {} # string after idx
        
        def dp(idx):
            if idx in memo:
                return memo[idx]
            
            if idx >= len(s):
                return 1
            
            if s[idx] == "0":
                return 0

            one = dp(idx+1)
            two = 0
            if idx + 1 < len(s):
                if s[idx:idx+2] <= "26":
                    two = dp(idx+2)

            memo[idx] = one + two
            return memo[idx]
            
        return dp(0)


            
            