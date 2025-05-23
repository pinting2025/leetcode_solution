class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        cost = [[row] * 10 for _ in range(col)]
        
        for r in range(row):
            for c in range(col):
                num = grid[r][c]
                cost[c][num] -= 1
            
        memo = {}

        def dp(idx, prev):
            if idx >= col:
                return 0
            
            if (idx, prev) in memo:
                return memo[(idx, prev)]
            
            temp = float('inf')
            for number, count in enumerate(cost[idx]):
                if number != prev:
                    temp = min(temp, dp(idx+1, number) + count)
            
            memo[(idx, prev)] = temp

            return memo[(idx, prev)]
        
        return dp(0, -1)

        # memo = {} # store the idx of each column

        # def dp(idx, prev):
        #     if (idx, prev) in memo:
        #         return memo[(idx, prev)]
            
        #     if idx >= len(grid[0]):
        #         return 0
            
        #     dic = defaultdict(int)
        #     for r in range(len(grid)):
        #         dic[grid[r][idx]] += 1
            
        #     temp = float('inf')
        #     for number in range(0, 10):
        #         if number != prev:
        #             temp = min(temp, len(grid) - dic[number] + dp(idx+1, number))
            
        #     memo[idx] = temp

        #     return memo[idx]
        
        # return dp(0, -1)
        

        