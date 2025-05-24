class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        w=[]
        for i,v in enumerate(words):
            for j in v:
                if j==x:
                   w.append(i) 
                   break
                else:
                    continue
        return w


        