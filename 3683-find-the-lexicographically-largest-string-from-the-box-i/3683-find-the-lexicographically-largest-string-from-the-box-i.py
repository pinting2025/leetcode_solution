class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # split the word into numFriends groups
        if numFriends == 1:
            return word

        target = len(word) - numFriends + 1
        largest = max(word)
        res = ""
        
        for i in range(len(word)):
            if word[i] == largest:
                temp = word[i:i+target] if i+target <= len(word) else word[i:]
                if temp > res:
                    res = temp
        
        return res
