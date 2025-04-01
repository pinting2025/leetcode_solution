class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dic_s = {}
        res = 0

        for i in range(len(s)):
            dic_s[s[i]] = dic_s.get(s[i], i)
        
        for i in range(len(t)):
            res += abs(i - dic_s[t[i]])
        
        return res

        