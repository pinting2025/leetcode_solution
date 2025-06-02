class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(min(limit+1, n+1)):
            left = n - i
            if left <= limit * 2:
                lower = max(left-limit, 0)
                upper = min(limit, left)
                res += upper - lower + 1
        
        return res

        # res = 0
        # for i in range(min(limit+1, n+1)):
        #     for j in range(min(limit+1, n+1-i)):
        #         if n-i-j <= limit:
        #             res += 1
        
        # return res