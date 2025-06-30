class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = Counter(nums)
        nums = sorted(set(nums))
        res = float('-inf')
        prev = nums[0]

        if len(nums) == 1:
            return 0

        for n in nums[1:]:
            if n - prev == 1:
                res = max(res, dic[n] + dic[prev])
            prev = n
        
        return res if res != float('-inf') else 0

