class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # [idx, t]
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                cidx, ctemp = stack.pop()
                res[cidx] = i - cidx
                
            stack.append([i, t])

        return res

            