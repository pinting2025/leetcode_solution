class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        left = 0
        right = 2
        res = 0

        while right < len(nums):
            if (nums[left] + nums[right]) * 2 == nums[left+1]:
                res += 1
            left += 1
            right += 1

        return res
        