class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        track = []
        res = []

        def backtrack(idx, val):
            if val == target:
                res.append(track.copy())
                return
            if val > target or idx >= len(candidates):
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                track.append(candidates[i])
                backtrack(i+1, val + candidates[i])
                track.pop()
        
        backtrack(0, 0)
        
        return res


            



        