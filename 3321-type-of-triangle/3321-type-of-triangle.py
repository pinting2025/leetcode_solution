class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums = sorted(nums)

        if nums[0] + nums[1] > nums[2]:
            cur = len(set(nums))
            if cur == 1:
                return "equilateral"
            elif cur == 2:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"
        