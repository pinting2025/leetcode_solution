class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start, track):
            nonlocal res
            res.append(track[:])

            for idx in range(start, len(nums)):
                if idx > start and nums[idx] == nums[idx-1]:
                    continue
                track.append(nums[idx])
                backtrack(idx+1, track)
                track.pop()

            return 
        
        backtrack(0, [])
        return res

