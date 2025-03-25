class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals = sorted(intervals)
        # res = []
        # cur = []

        # for i in intervals:
        #     if res == []:
        #         res.append(i)
        #         cur = res[-1]
        #     if i[0] >= cur[0] and i[1] <= cur[1]:
        #         continue
        #     elif i[0] > cur[1]:
        #         res.append(i)
        #         cur = res[-1]
        #     else:
        #         if i[1] > cur[1]:
        #             res[-1][1] = i[1]
        #             cur[1] = i[1]
        #         if i[0] < cur[0]:
        #             res[-1][0] = i[0]
        #             cur[0] = i[0]
        # return res    
        if not intervals:
            return []

        intervals = sorted(intervals)
        res = [intervals[0]]

        for i in intervals[1:]:
            cur = res[-1]
            start, end = cur[0], cur[1]

            if i[0] <= cur[1]:
                res[-1][1] = max(i[1], res[-1][1])
            else:
                res.append(i)

        return res

       