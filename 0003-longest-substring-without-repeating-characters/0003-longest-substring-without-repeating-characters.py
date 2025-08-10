class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = left
        dic = set()
        res = 0

        while left <= right and right < len(s):
            if s[right] in dic:
                res = max(right-left, res)
                while s[left] != s[right]:
                    dic.remove(s[left])
                    left += 1
                left += 1
            dic.add(s[right])
            right += 1

        return max(res, right - left)








