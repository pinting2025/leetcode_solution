class Solution:
    def countLargestGroup(self, n: int) -> int:
        def count_digit(num):
            num = str(num)
            cur = 0
            for d in num:
                cur += int(d)
            return cur
        
        counter = Counter()
        max_num = 1
        res = 0

        for i in range(1, n+1):
            cur = count_digit(i)
            counter[cur] += 1
            if counter[cur] > max_num:
                res = 1
                max_num = counter[cur]
            elif counter[cur] == max_num:
                res += 1
        
        return res


                
        