class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        cur = max_diff = min_diff = 0

        for d in differences:
            cur += d
            max_diff = max(max_diff, cur)
            min_diff = min(min_diff, cur)
        
        res = (upper - max_diff) - (lower - min_diff) + 1

        return res if res > 0 else 0

        # max_diff = max(differences)
        # min_diff = min(differences)
        # if abs(max_diff) > upper - lower or abs(min_diff) > upper - lower:
        #     return 0
        
        # res = 0
        # for i in range(lower, upper+1):
        #     flag = True
        #     cur = i
        #     for j in differences:
        #         if cur + j < lower or cur + j > upper:
        #             flag = False

        #         if flag == False:
        #             break
        #         cur += j

        #     if flag == True:
        #         res += 1
        
        # return res
            
            
                

        