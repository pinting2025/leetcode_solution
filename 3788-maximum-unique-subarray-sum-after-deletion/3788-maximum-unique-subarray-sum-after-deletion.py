class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # make the array unique
        nums = set(nums)
        ans = 0

        # if all negative
        neg = float('-inf')

        for i in nums:
            if i > 0:
                ans += i

            elif i > neg:
                neg = i

        if ans == 0:
            return neg
    
        return ans


        