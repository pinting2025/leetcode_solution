class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flatten = []
        for r in grid:
            for c in r:
                flatten.append(c)
        flatten.sort()
        
        remainder = flatten[0] % x
        for i in flatten[1:]:
            if i % x != remainder:
                return -1
        
        def count_step(target):
            count = 0
            for i in flatten:
                count += abs(i - target) // x
            return count

        median = len(flatten) // 2
        return count_step(flatten[median])



        
        