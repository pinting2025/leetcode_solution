class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        
        s = s.lower()
        s = re.sub(r"[^a-z^A-Z^0-9]", "", s)
        
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
        