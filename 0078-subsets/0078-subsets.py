class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])

        def backtrack(target_len, start, track):
            if len(track) == target_len:
                res.append(track[:])
                return 
            
            end = len(nums) - (target_len - len(track))

            for idx in range(start, end+1):
                track.append(nums[idx])
                backtrack(target_len, idx+1, track)
                track.pop()
            
            return 
        
        for i in range(1,len(nums)+1):
            backtrack(i, 0, [])
        
        return res




        