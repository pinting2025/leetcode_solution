class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])

        prev = nums[0]
        res = float('-inf')

        for n in nums[1:]:
            res = max(res, abs(n-prev))
            prev = n
        
        return res
