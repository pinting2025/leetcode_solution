class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, track):
            if len(track) == k and sum(track) == n:
                res.append(track[:])
                return 
            
            if len(track) >= k or sum(track) >= n:
                return 
            
            for idx in range(start, 10):
                track.append(idx)
                backtrack(idx+1, track)
                track.pop()
            
            return 
        
        backtrack(1, [])
        return res
                

            
            
            


        