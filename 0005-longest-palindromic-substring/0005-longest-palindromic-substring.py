class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = []
        max_length = 1
        start = 0

        def helper(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i + 1, j - i - 1
            
        for i in range(len(s)):
            # odd
            left, length = helper(i, i)
            if length > max_length:
                start = left
                max_length = length
            
            # even
            left, length = helper(i, i+1)
            if length > max_length:
                start = left
                max_length = length
        
        return s[start:start+max_length]





            
