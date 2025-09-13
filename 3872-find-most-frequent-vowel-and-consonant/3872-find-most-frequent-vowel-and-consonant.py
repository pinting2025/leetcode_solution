class Solution:
    def maxFreqSum(self, s: str) -> int:
        string = list(s)
        vowels = {"a", "e", "i", "o", "u"}

        freq = Counter(string)
        vol_sum = 0
        const_sum = 0

        for letter in freq:
            count = freq[letter]
            if letter in vowels and vol_sum < count:
                vol_sum = count
            elif letter not in vowels and const_sum < count:
                const_sum = count
        
        return vol_sum + const_sum


                
