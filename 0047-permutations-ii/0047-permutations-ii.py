class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        dic = Counter(nums)
        used = Counter()

        def backtrack(track):
            if len(track) == len(nums):
                res.append(track[:])
                return
            
            for k in dic:
                if used[k] + 1 > dic[k]:
                    continue
                
                used[k] += 1
                track.append(k)
                backtrack(track)
                track.pop()
                used[k] -= 1
        
        backtrack([])

        return res

