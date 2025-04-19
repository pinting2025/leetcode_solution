class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def count(t: int) -> int:
            i = res = 0 ; j = bisect_right(nums, t - nums[0]) - 1
            while i < j:
                if nums[i] + nums[j] > t:   j -= 1
                else:   res += j-i ; i += 1
            return res
        nums.sort()
        return count(upper) - count(lower - 1)