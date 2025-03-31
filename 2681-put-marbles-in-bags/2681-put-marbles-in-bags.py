class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if len(weights) == k:
            return 0
        
        values = []
        for i in range(len(weights)-1):
            values.append(weights[i] + weights[i+1])
        
        values.sort()
        mini = sum(values[0:k-1])
        maxi = sum(values[len(values) - k+1:])
        
        return sum(values[len(values) - k+1:]) - sum(values[0:k-1])

        