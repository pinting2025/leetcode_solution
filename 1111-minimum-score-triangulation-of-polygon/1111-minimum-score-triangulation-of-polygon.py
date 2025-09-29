class Solution:
    def __init__(self):
        self.dp = [[0] * 50 for _ in range(50)]

    def minScoreTriangulation(self, values, i=0, j=0, res=0):
        if j == 0:
            j = len(values) - 1
        if self.dp[i][j] != 0:
            return self.dp[i][j]
        for k in range(i + 1, j):
            res = min(res if res != 0 else float('inf'),
                self.minScoreTriangulation(values, i, k) +
                values[i] * values[k] * values[j] +
                self.minScoreTriangulation(values, k, j))
        self.dp[i][j] = res
        return self.dp[i][j]

        # def reform(arr, idx):
        #     new_arr = arr[idx:] + arr[:idx]
        #     return new_arr
        
        # def times(arr):
        #     temp = 1
        #     for a in arr:
        #         temp *= a
        #     return temp 

        # res = float('inf')
        # for i in range(len(values)//2):
        #     cur_count = 0
        #     cur_arr = reform(values, i)
        #     cur_arr.append(cur_arr[0])
        #     left = 0
        #     right = 2
        #     while left < right and right < len(values):
        #         cur_count += times(cur_arr[left:right+1])
        #         left = right
        #         right = left + 2
        #     if cur_count < res:
        #         res = cur_count
        
        # return res
        

