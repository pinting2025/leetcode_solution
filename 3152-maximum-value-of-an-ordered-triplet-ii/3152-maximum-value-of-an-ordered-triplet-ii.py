class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        left = 0
        right = 1
        cal_1 = {}

        while left < right and right < len(nums):
            cal_1[right] = cal_1.get(right, nums[left] - nums[right])

            if nums[left] < nums[right]:
                left = right

            right += 1
        
        cal_2 = [0] * len(nums)
        cal_2[-1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > cal_2[i+1]:
                cal_2[i] = nums[i]
            else:
                cal_2[i] = cal_2[i+1]

        res = 0
        for idx in cal_1:
            val = cal_1[idx]
            if val <= 0:
                continue

            if idx < len(nums) - 1:
                cur = val * cal_2[idx+1]
                if cur > res:
                    res = cur
        
        return res