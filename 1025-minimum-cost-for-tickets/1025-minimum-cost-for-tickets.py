class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        last_day = days[-1]
        days = set(days)

        def dp(idx):
            if idx > last_day:
                return 0
            
            if idx in memo:
                return memo[idx]
            
            if idx not in days:
                memo[idx] = dp(idx+1)
                return memo[idx]
            
            one = costs[0] + dp(idx+1)
            seven = costs[1] + dp(idx+7)
            thrity = costs[2] + dp(idx+30)
            
            memo[idx] = min(one, seven, thrity)

            return memo[idx]
        
        return dp(1)



            