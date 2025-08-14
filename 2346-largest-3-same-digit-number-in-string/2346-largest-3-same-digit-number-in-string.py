class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for d in "9876543210":
            if d*3 in num:
                return d*3
        
        return ""
        
        # count = 1
        # prev = num[0]
        # for d in num[1:]:
        #     print(d)
        #     print(prev)
        #     while d == prev:
        #         count += 1
        #     if count == 3:
        #         return d*3
        #     else:
        #         count = 1
        #         prev = d
        
        # return ""
            
            

        


        