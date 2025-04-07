class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        left = 0

        for i in range(1, len(prices)):
            res = max(res, prices[i] - prices[left])
            if prices[i] < prices[left]:
                left = i
        
        return res

        