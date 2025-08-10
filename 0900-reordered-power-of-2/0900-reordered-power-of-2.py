class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # list out all permutations
        used = Counter(str(n))

        def helper(n):
            while n != 1 and n % 2 == 0:
                n /= 2
            return True if n == 1 else False
            
        def backtrack(track):
            if len(track) == len(str(n)):
                track = "".join(track)
                return helper(int(track))
            
            for k in used.keys():
                if used[k] == 0:
                    continue
                
                if len(track) == 0 and k == '0':
                    continue
                
                used[k] -= 1
                track.append(k)
                if backtrack(track):
                    return True
                track.pop()
                used[k] += 1
            
            return False
        
        return backtrack([])


                

            

                
