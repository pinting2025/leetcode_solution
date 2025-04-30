class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        track = []
        res = 0

        def backtrack(idx):
            nonlocal res
            cur = 0
            for i in track:
                cur ^= i
            
            res += cur

            if idx >= len(nums):
                return
            
            for i in range(idx, len(nums)):
                track.append(nums[i])
                backtrack(i+1)
                track.pop()

        backtrack(0)

        return res

