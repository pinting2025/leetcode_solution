class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        
        res = 0
        nums = set(nums)
        if k in nums:
            return len(nums) - 1
        else:
            return len(nums)
            

