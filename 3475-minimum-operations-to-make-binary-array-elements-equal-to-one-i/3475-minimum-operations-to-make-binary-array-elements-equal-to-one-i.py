class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def flip(r):
            if nums[r] == 0:
                nums[r] = 1
            else:
                nums[r] = 0
        
        c = 0
        for r in range(len(nums)-2):
            if nums[r] == 0:
                c += 1
                flip(r)
                flip(r+1)
                flip(r+2)

        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        
        return c


                
            
        