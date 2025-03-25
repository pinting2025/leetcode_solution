class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []
        cur = []

        for i in intervals:
            if res == []:
                res.append(i)
                cur = res[-1]
            if i[0] >= cur[0] and i[1] <= cur[1]:
                continue
            elif i[0] > cur[1]:
                res.append(i)
                cur = res[-1]
            else:
                if i[1] > cur[1]:
                    res[-1][1] = i[1]
                    cur[1] = i[1]
                if i[0] < cur[0]:
                    res[-1][0] = i[0]
                    cur[0] = i[0]
        return res    




                
            