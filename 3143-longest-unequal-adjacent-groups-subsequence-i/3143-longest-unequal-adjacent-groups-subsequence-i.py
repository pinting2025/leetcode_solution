class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        cur = groups[0]
        res = []
        res.append(words[0])

        for w, b in zip(words[1:], groups[1:]):
            if b != cur:
                res.append(w)
                cur = b
        
        return res
        




        return 