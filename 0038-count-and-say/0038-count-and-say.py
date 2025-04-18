class Solution:
    def countAndSay(self, n: int) -> str:
        memo = {}

        def dp(n):
            if n == 1:
                return '1'
            
            if n in memo:
                return memo[n]
            
            arr = dp(n-1)
            count = 1
            prev = arr[0]

            stack = []
            for i in arr[1:]:
                if i == prev:
                    count += 1
                else:
                    stack.append(str(count))
                    stack.append(prev)
                    count = 1
                    prev = i

            stack.append(str(count))
            stack.append(prev)

            res = ''.join(stack)
            memo[n] = res

            return res
        
        return dp(n)

                

            

            

