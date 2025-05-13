class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10 ** 9 + 7
        count = [0] * 27
        for i in s:
            count[ord('z') - ord(i) + 1] += 1
        
        while t > 0:
            idx, val = 0, 0
            for i, c in enumerate(count):
                if val == 0 and c > 0:
                    idx, val = i, c
                    break
            
            if t < idx:
                break
                
            count[idx] = 0
            t -= idx
            for i in range(idx + 1, 27):
                count[i - idx] = count[i]
                count[i] = 0
            count[25] += val
            count[26] += val
        
        return sum(count) % mod