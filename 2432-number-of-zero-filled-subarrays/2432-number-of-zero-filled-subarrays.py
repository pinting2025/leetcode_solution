class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        dic = {}
        cur_count = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                cur_count += 1
            elif cur_count != 0:
                res += ((1+cur_count) * cur_count) // 2
                cur_count = 0
        
        if cur_count != 0:
            res += ((1+cur_count) * cur_count) // 2
            
        return res



