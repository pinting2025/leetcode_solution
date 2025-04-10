class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        low = str(start)
        high = str(finish)

        n = len(high)
        low = low.zfill(n)  # Pad zeros on left of low until len(low) reaches n
        pre_len = n - len(s)  # Number of prefix digits we can freely choose
        
        memo = {}
        def dp(i, limit_low, limit_high):
            key = (i, limit_low, limit_high)
            if key in memo:
                return memo[key]
                
            if i == n:
                return 1
            
            lo = int(low[i]) if limit_low else 0  # Lower digit bound
            hi = int(high[i]) if limit_high else 9  # Upper digit bound
            res = 0
            
            if i < pre_len:
                for digit in range(lo, min(hi, limit) + 1):
                    res += dp(i + 1, limit_low and digit == lo, limit_high and digit == hi)
            else:
                x = int(s[i - pre_len])
                if lo <= x <= min(hi, limit):
                    res = dp(i + 1, limit_low and x == lo, limit_high and x == hi)
            
            memo[key] = res
            return res
        
        return dp(0, True, True)