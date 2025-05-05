class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        res = 1
        nums = set(nums)

        for i in nums:
            if i-1 not in nums:
                cur = 1

                while i+1 in nums:
                    cur += 1
                    i += 1
                res = max(res, cur)
        
        return res


