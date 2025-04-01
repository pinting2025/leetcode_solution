class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        counts = Counter()

        def game():
            n1 = arr[0]
            n2 = arr[1]

            if n1 > n2:
                counts[n1] += 1
                arr.pop(1)
                arr.append(n2)
                return n1
            else:
                counts[n2] += 1
                arr.pop(0)
                arr.append(n1)
                return n2

        cur = game()
        while counts[cur] < k:
            if counts[cur] > len(arr):
                break
            cur = game()
        
        return cur
        
        




        