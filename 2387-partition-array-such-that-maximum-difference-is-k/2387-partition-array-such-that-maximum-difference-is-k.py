class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        lower = nums[0]
        res = 0

        for i in range(len(nums)):
            print(nums[i], lower)
            if nums[i] - lower <= k:
                continue
            else:
                lower = nums[i]
                res += 1
            
        return res + 1

            

            

            