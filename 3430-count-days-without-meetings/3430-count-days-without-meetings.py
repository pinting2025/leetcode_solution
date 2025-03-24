class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # flag = [False] * (days + 1)
        # flag[0] = True

        # for m in meetings:
        #     for d in range(m[0], m[1]+1):
        #         flag[d] = True
        
        # return flag.count(False)

        meetings = sorted(meetings)
        free = 1
        res = 0
        for i in range(len(meetings)):
            m = meetings[i]
            if m[0] > free:
                res += m[0] - free

            free = max(free, m[1] + 1)
        
            if i == len(meetings) - 1:
                if free <= days:
                    res += days - free + 1
            
        return res

        

        



