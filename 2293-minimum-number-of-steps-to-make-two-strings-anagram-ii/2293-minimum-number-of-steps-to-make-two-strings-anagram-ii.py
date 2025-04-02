class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s, count_t = Counter(s), Counter(t)

        res = 0
        for i in count_s:
            cur_s = count_s[i]
            cur_t = count_t[i]
            if cur_s > cur_t:
                res += abs(cur_s - cur_t)
        
        for i in count_t:
            cur_s = count_s[i]
            cur_t = count_t[i]
            if cur_t > cur_s:
                res += abs(cur_s - cur_t)
        
        return res


        