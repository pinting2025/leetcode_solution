class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        track = [0] * n
        palindromic = []

        def backtrack(idx):
            if idx >= (n+1) // 2:
                cur = track.copy()
                cur = map(str, cur)
                palindromic.append(''.join(cur))
                return 
            
            s = 0 if idx > 0 else 1

            for i in range(s, 10):
                track[idx] = i
                track[n-idx-1] = i
                backtrack(idx+1)

        backtrack(0)

        def cal_perm(appear, val):
            for i in appear.values():
                if i >= 2:
                    val /= factorial(i)
            return int(val)

        res = 0
        visited = set()
        for num in palindromic:     
            val = 0

            if int(num) % k == 0:
                check = ''.join(sorted(num))
                if check in visited:
                    continue
                visited.add(check)
                appear = Counter(num)
                val = cal_perm(appear, factorial(n))
                if '0' in appear:
                    appear['0'] -= 1
                    val_0 = cal_perm(appear, factorial(n-1))
                    val -= val_0
                res += val 
        return res

