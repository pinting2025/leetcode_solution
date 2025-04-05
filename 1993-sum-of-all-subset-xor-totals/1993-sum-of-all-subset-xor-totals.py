class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        track = []
        res = 0

        def backtrack(idx):
            nonlocal res
            temp = 0
            for i in track:
                temp ^= i

            res += temp

            if idx >= len(nums):
                return
            
            for i in range(idx, len(nums)):
                track.append(nums[i])
                backtrack(i+1)
                track.pop()
        
        backtrack(0)

        return res
        

        
        