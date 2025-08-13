class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, track):
            if len(track) == k:
                res.append(track[:])
                return 
            
            end = n - (k-len(track)) + 1

            for idx in range(start, end+1):
                track.append(idx)
                backtrack(idx+1, track)
                track.pop()
            return 
        
        backtrack(1, [])

        return res
            
