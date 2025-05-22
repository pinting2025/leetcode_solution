class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # if length costs is larger than candidates * 2, create left and right array and store the remain array
        res = 0
        if len(costs) > candidates*2:
            left = costs[0:candidates]
            right = costs[-candidates:]
            remain = costs[candidates:-candidates]
            heapq.heapify(left)
            heapq.heapify(right)

            idx_left = 0
            idx_right = len(remain) - 1

            while idx_left <= idx_right and k > 0:
                if left[0] <= right[0]:
                    res += heapq.heappop(left)
                    heapq.heappush(left, remain[idx_left])
                    idx_left += 1
                else:
                    res += heapq.heappop(right)
                    heapq.heappush(right, remain[idx_right])
                    idx_right -= 1
                k -= 1
            
            temp = left + right
            heapq.heapify(temp)
            while k > 0:
                res += heapq.heappop(temp)
                k -= 1
            return res
        else:
            # for each round, pop the min value using heapify
            heapq.heapify(costs)
            while k > 0:
                res += heapq.heappop(costs)
                k -= 1
            return res

