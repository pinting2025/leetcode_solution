class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        texts = text.split(" ")
        brokenLetters = set(brokenLetters)
        res = 0

        for word in texts:
            if set(word).isdisjoint(brokenLetters):
                res += 1
    
        return res
        


