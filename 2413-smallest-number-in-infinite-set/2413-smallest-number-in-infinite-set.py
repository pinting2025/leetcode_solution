class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.minheap = []
        self.add_back = set()
        
    def popSmallest(self) -> int:
        if self.minheap:
            item = heapq.heappop(self.minheap)
            self.add_back.remove(item)
            return item
        else:
            val = self.current
            self.current += 1
            return val
            
    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.add_back:
            heapq.heappush(self.minheap, num)
            self.add_back.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)