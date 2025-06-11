class Solution:
    def maxDifference(self, s: str) -> int:
        dic = Counter(s)

        odd = float('-inf')
        even = float('inf')

        for i, val in dic.items():
            if val % 2 == 0:
                even = min(even, val)
            else:
                odd = max(odd, val)
        
        return odd - even 