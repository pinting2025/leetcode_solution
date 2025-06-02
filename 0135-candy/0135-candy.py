class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
            
        dic = sorted([(r, idx) for idx, r in enumerate(ratings)], reverse = True)
        res = [1] * len(ratings)
        
        for i in range(len(dic)-1, -1, -1):
            r, idx = dic[i]

            # not edge
            if idx > 0 and idx < len(ratings) - 1:
                # larger than both side
                if r > ratings[idx-1] and r > ratings[idx+1]:
                    res[idx] = max(res[idx-1], res[idx+1]) + 1
                
                elif r > ratings[idx-1]:
                    res[idx] = res[idx-1] + 1
            
                elif r > ratings[idx+1]:
                    res[idx] = res[idx+1] + 1
            
            elif idx == 0:
                if ratings[idx] > ratings[idx+1]:
                    res[idx] = res[idx+1] + 1
            
            elif idx == len(ratings)-1:
                if ratings[idx] > ratings[idx-1]:
                    res[idx] = res[idx-1] + 1
                
        return sum(res)






            



