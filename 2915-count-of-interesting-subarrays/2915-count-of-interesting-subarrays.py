class Solution:
    def countInterestingSubarrays(self, nums: List[int], mod: int, k: int) -> int:
        n = len(nums)
        count = Counter([0])
        curr = 0

        res = 0
        for num in nums:
            # Current total cnt
            if num % mod == k: curr += 1
            
            # curr - k = count to remove
            # +mod for normalization
            # Like say if curr is 7 and k is 3, we need to minus 4 from 7
            # So we need to find how many subarrays have a cnt of 4 
            res += count[(curr - k + mod) % mod]
            count[curr % mod] += 1
        return res