class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = nums[0]

        for n in nums:
            target |= n
        
        def backtrack(idx, cur):
            if idx == len(nums):
                return 1 if cur == target else 0
            
            return backtrack(idx+1, cur | nums[idx]) + backtrack(idx+1, cur)
        
        return backtrack(0, 0)