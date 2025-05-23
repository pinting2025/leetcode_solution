class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = set(days)
        memo = {} # idx, day index

        def dp(idx):
            if idx > 365:
                return 0
            
            if idx in memo:
                return memo[idx]
            
            if idx not in days:
                memo[idx] = dp(idx+1)
            
            else:
                one = costs[0] + dp(idx+1)
                seven = costs[1] + dp(idx+7)
                thrity = costs[2] + dp(idx+30)

                memo[idx] = min(one, seven, thrity)

            return memo[idx]

        return dp(0)
        