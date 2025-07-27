class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        left = 0
        cur = 1
        res = 0

        while left < cur and cur < len(nums) - 1:
            if nums[cur] != nums[cur+1]:
                if nums[left] < nums[cur] and nums[cur+1] < nums[cur]:
                    res += 1
                elif nums[left] > nums[cur] and nums[cur+1] > nums[cur]:
                    res += 1
                left = cur
                cur += 1
            else:
                cur += 1
        
        return res