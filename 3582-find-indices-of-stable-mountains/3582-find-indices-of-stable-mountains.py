class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        prev = height[0]
        res = []

        for i in range(1, len(height)):
            if prev > threshold:
                res.append(i)
            prev = height[i]
        
        return res



