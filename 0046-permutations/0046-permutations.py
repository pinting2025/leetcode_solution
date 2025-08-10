class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        def backtrack(idx, track):
            if len(track) == len(nums):
                res.append(track[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue

                seen.add(nums[i])
                track.append(nums[i])
                backtrack(i, track)
                track.pop()
                seen.remove(nums[i])

        backtrack(0, [])
        
        return res
            

