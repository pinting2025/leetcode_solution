class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        track = []
        res = []

        def backtrack(idx, val):
            if val == target:
                res.append(track.copy())
                return

            if idx >= len(candidates) or val > target:
                return
            
            for i in range(idx, len(candidates)):
                track.append(candidates[i])
                backtrack(i, val + candidates[i])
                track.pop()
    
        backtrack(0,0)

        return res








        # if target < min(candidates):
        #     return []
        
        # candidates = set(candidates)
        # res = []
        # temp = []

        # for c in candidates:
        #     m = 1
        #     candidates.remove(c)
        #     while c * m <= target:
        #         if (target - c * m in candidates) or (target == c * m):
        #             for i in range(m):
        #                 temp.append(c)
        #             if target - c * m != 0:
        #                 temp.append(target - c * m)
        #             if sorted(temp) not in res:
        #                 res.append(sorted(temp))
        #             temp = []
        #         m += 1
        #     candidates.add(c)
        
        # return res

