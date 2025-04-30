class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers = Counter(answers)
        
        res = 0
        for c, a in answers.items():
            if c == 0:
                res += a

            elif c+1 >= a:
                res += (c + 1)

            else:
                r = a % (c+1)
                if r != 0:
                    res += a + (c+1) - r
                else:
                    res += a
        return res

