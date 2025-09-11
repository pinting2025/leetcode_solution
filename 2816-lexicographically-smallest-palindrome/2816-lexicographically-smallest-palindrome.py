class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left, right = 0, len(s)-1
        res = [''] * len(s)

        while left <= right:
            if s[left] != s[right]:
                if s[left] < s[right]:
                    res[right] = s[left]
                    res[left] = s[left]
                else:
                    res[right] = s[right]
                    res[left] = s[right]
            else:
                res[left] = s[left]
                res[right] = s[right]
            left += 1
            right -= 1
        return "".join(res)
        


