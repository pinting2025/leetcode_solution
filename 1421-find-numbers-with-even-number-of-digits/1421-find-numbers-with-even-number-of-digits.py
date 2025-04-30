class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            n = str(n)
            if len(n) % 2 == 0:
                res += 1
        return res
