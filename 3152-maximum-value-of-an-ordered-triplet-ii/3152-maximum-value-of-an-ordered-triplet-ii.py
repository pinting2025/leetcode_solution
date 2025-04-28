class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_diff = 0
        max_i = 0
        max_value = 0

        for i in range(len(nums)):
            max_value = max(max_value, max_diff * nums[i])
            max_diff = max(max_diff, max_i - nums[i])
            max_i = max(max_i, nums[i])
        
        return max_value