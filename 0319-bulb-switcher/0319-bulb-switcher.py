class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))
        
        # res = 0
        # for i in range(1, n+1):
        #     if sqrt(i) == int(sqrt(i)):
        #         res += 1
        # return res

        # res = 0
        # for i in range(1, n+1):
        #     factor = 0
        #     for j in range(1, i+1):
        #         if i % j == 0:
        #             factor += 1
        #     if factor % 2 == 1:
        #         res += 1
        # return res
