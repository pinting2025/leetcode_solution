class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drink = 0

        while numBottles - numExchange >= 0:
            numBottles -= numExchange
            drink += numExchange
            numBottles += 1
            numExchange += 1
        
        drink += numBottles

        return drink
        


