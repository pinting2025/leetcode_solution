class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        memo = {}

        memo[1] = [1]
        if numRows >= 2:
            memo[2] = [1,1]

        def dp(i):
            if i in memo:
                return memo[i]
            
            prev = dp(i-1)
            temp = [1]

            for k in range(1, i-1):
                temp.append(prev[k - 1] + prev[k])
            
            temp.append(1)
            memo[i] = temp

            return temp
        
        res = []

        for i in range(1, numRows+1):
            res.append(dp(i))

        return res
            


                

        
