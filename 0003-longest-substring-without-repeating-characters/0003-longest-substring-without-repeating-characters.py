class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
            
        dic = set()
        res = 1
        left = 0

        for right in range(len(s)):
            while s[right] in dic:
                dic.remove(s[left])
                left += 1
            
            dic.add(s[right])
                
            res = max(res, right-left+1)
            if res == len(set(s)):
                return res
        
        return res
