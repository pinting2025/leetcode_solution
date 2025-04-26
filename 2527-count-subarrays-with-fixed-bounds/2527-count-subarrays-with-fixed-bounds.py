class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        min_i, max_i, bad_i = -1, -1, -1
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                bad_i = i
            if nums[i] == minK: min_i = i
            if nums[i] == maxK: max_i = i
            res += max(0, min(min_i, max_i) - bad_i)
        return res