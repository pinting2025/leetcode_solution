class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        target = sorted(nums, reverse = True)
        target = target[:k]
        res = []
        
        for n in nums:
            if n in target:
                res.append(n)
                target.remove(n)
            if len(res) == k:
                return res



