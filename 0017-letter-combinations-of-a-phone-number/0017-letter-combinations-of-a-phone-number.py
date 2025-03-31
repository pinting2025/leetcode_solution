class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        nums = '23456789'
        letters = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        dic = {nums[i] : letters[i] for i in range(8)}
    
        track = []
        res = []
        def backtrack(layer):
            nonlocal track
            if layer == len(digits):
                res.append("".join(track))
                return
            
            for i in dic[digits[layer]]:
                track.append(i)
                backtrack(layer+1)
                track.pop()
    
        backtrack(0)
        return res

