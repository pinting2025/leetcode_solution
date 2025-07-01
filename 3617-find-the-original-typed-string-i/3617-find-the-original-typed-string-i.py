class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev = word[0]
        res = 0

        for c in word[1:]:
            if c == prev:
                res += 1
            else:
                prev = c
        
        return res + 1