class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        res = 0
        
        for i in range(len(points)):
            upper = points[i][1]
            lower = float('-inf')

            for j in range(i+1, len(points)):
                cur = points[j][1]
                if cur <= upper and cur > lower:
                    res += 1
                    lower = cur
                    if cur == upper:
                        break
        
        return res
