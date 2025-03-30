class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        appear = Counter(s)

        left = 0
        right = 0
        res = []

        cur_element = Counter()

        while right < len(s):
            if s[right] in cur_element:
                cur_element[s[right]] -= 1
            else:
                cur_element[s[right]] += appear[s[right]] - 1
            
            right += 1

            if sum(cur_element.values()) == 0:
                res.append(right-left)
                left = right
        
        return res
                

            
        
        
       

        