class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        appear = Counter(s)
        cur_element = Counter()

        left = 0
        right = 0
        remain = 0
        res = []

        while right < len(s):
            if cur_element[s[right]] == 0:
                cur_element[s[right]] += appear[s[right]] - 1
                remain += cur_element[s[right]]
            else:
                cur_element[s[right]] -= 1
                remain -= 1
            
            right += 1

            if remain == 0:
                res.append(right-left)
                left = right
                cur_element.clear()

        return res
                

            
        
        
       

        