class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for num in range(low, high+1):
            num = str(num)

            if len(num) % 2 != 0:
                continue
            
            length = len(num) // 2
            f = num[:length]
            s = num[length:]

            def cal(lis):
                cur = 0
                for i in lis:
                    cur += int(i)
                return cur
            
            if cal(f) == cal(s):
                count += 1
            
        return count
                







        