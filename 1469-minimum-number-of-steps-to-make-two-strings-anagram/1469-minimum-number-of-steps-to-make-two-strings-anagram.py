class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        
        res = 0
        for i in count_s:
            cur_s = count_s[i]
            cur_t = count_t[i]
            if cur_s > cur_t:
                res += abs(cur_t - cur_s)
        
        return res


