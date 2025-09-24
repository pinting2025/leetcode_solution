class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'

        res = []
        
        # deal with sign
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            res.append('-')
        
        numerator = abs(numerator)
        denominator = abs(denominator)

        # get the integal part
        integer = numerator // denominator
        res.append(str(integer))

        # reminder
        reminder = numerator % denominator
        if reminder == 0:
            return str("".join(res))
        
        res.append('.')
        seen = {}

        while reminder != 0:
            if reminder in seen:
                res.insert(seen[reminder], '(')
                res.append(')')
                break
            
            seen[reminder] = len(res)
            reminder *= 10
            res.append(str(reminder // denominator))
            reminder %= denominator

        return "".join(res)
