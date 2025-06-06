class Solution:
    def robotWithString(self, s: str) -> str:
        dic = Counter(s)
        t = []
        p = []

        # get next char
        def search():
            for i in range(26):
                c = chr(ord('a') + i)
                if dic.get(c, 0) > 0:
                    return c
            return '{'

        # next_char = search(char)

        for char in s:
            t.append(char)
            dic[char] -= 1
            while t and t[-1] <= search():
                p.append(t.pop())

        while t:
            p.append(t.pop())

        return "".join(p)
        




        
        