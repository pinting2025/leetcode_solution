class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
        current_vowels = []

        for letter in s:
            if letter in vowels:
                 current_vowels.append(letter)

        current_vowels.sort()

        res = []
        i = 0
        for letter in s:
            if letter not in vowels:
                res.append(letter)
            else:
                res.append(current_vowels[i])
                i += 1
        
        return "".join(res)
