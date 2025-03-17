class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = Counter()

        for i in nums:
            dic[i] += 1
        
        print(dic)
        
        for i in dic:
            if dic[i] % 2 != 0:
                return False 
        
        return True
            



        