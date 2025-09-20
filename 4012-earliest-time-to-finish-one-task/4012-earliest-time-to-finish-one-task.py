class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        res = float('inf')
        for start, finish in tasks:
            if start+finish < res:
                res = start+finish
        
        return res

