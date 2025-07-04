class Solution:
    def kthCharacter(self, k: int) -> str:
        res = ['a']

        while len(res) < k:
            time = len(res)
            for i in range(time):
                c = res[i]
                if c == 'z':
                    temp = 'a'
                else:
                    temp = chr(ord(c) + 1)
                res.append(temp)

        return res[k-1]

