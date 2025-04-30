class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        while len(set(nums)) != len(nums):
            if len(nums) >= 3:
                nums = nums[3:]
                res += 1
            else:
                res += 1
                return res
        
        return res