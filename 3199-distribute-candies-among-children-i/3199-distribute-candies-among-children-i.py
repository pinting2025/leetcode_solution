class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(min(limit+1, n+1)):
            for j in range(min(limit+1, n+1-i)):
                if n-i-j <= limit:
                    res += 1
        
        return res
