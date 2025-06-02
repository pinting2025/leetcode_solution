class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        start = points[0][0]
        end = points[0][1]
        res = 1

        for pos in points[1:]:
            s = pos[0]
            e = pos[1]

            if s >= start and s <= end:
                end = min(end, e)
                start = min(start, s)
            else:
                res += 1
                start = s
                end = e
        
        return res