class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        lower = nums[0]
        res = 0

        for n in nums:
            if n - lower > k:
                lower = n
                res += 1
            
        return res + 1

            

            

            