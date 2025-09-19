class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        digits = Counter(list(secret))

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
                digits[s] -= 1

        for s, g in zip(secret, guess):
            if s != g:
                if g in digits and digits[g] != 0:
                    cows += 1
                    digits[g] -= 1
        
        return str(bulls) + 'A' + str(cows) + 'B'
    
