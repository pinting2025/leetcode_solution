class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
    
        for i in range(100, 1000, 2):
            dic = Counter(digits)
            h = i // 100
            t = (i - h * 100) // 10
            s = (i - h * 100 - t * 10)
            
            dic[h] -= 1
            dic[t] -= 1
            dic[s] -= 1

            if min(dic.values()) >= 0:
                res.append(i)
        
        return sorted(res)


        # track = []
        # res = []

        # def backtrack(idx):
        #     if len(track) == 3:
        #         if track[0] != 0 and (track[0] * 100 + track[1] * 10 + track[2]) % 2 == 0:
        #             res.append(track[0] * 100 + track[1] * 10 + track[2])
        #             return 
            
        #     for i in range(len(digits)):
        #         track.append(digits[i])
        #         backtrack(i+1)
        #         track.pop()
        #     return

        # backtrack(0)

        # return res


        