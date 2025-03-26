class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flatten = []
        for r in grid:
            for c in r:
                flatten.append(c)
        flatten.sort()
        
        def is_valid(x):
            remainder = flatten[0] % x
            for i in flatten[1:]:
                if i % x != remainder:
                    return False
            return True
        
        def count_step(target):
            count = 0
            for i in flatten:
                count += abs(i - target) // x
            return count
        
        if not is_valid(x):
            return -1
        else:
            res = float('inf')
            mid = len(flatten) // 2
            while mid < len(flatten):
                if count_step(flatten[mid]) < res:
                    res = count_step(flatten[mid])
                    mid += 1
                else:
                    break
            return res



        
        