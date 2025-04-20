class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        count = Counter()
        for i in answers:
            if i == 0:
                res += 1
                continue

            if i not in count:
                count[i] = i
                res += (i + 1)
            else:
                count[i] -= 1
                if count[i] == 0:
                    del count[i]

        return res