class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # Preparation
        n = len(nums)
        queries.sort(key = lambda x: [x[0], x[1]])

        # Defining variables for solution
        size = len(queries)
        diff = [0] * (len(nums) + 1)
        left, curr = 0, 0
        res = []

        # Main Iteration
        for i, num in enumerate(nums):
            curr += diff[i]
            while left < size and queries[left][0] <= i:
                heappush(res, -queries[left][1])
                left += 1
            
            while res and curr < num and -res[0] >= i:
                curr += 1
                temp = -heapq.heappop(res)
                diff[temp + 1] -= 1

            if curr < num: 
                return -1
                
        return len(res)


        # queries = sorted(queries, key = lambda k: (k[0], -k[1]))
    
        # def helper(k):
        #     dec = [0] * (len(nums)+1)
        #     for start, end in queries[:k]:
        #         dec[start] += 1
        #         dec[end+1] -= 1
            
        #     cur = 0
        #     for i in range(len(nums)):
        #         cur += dec[i]
        #         if nums[i] - cur > 0:
        #             return False
        #     return True

        # left, right = 0, len(queries)
        # while left < right:
        #     mid = (left + right) // 2
        #     if helper(mid):
        #         right = mid
        #     else:
        #         left = mid + 1

        # return len(queries) - left if left <= len(queries) and helper(left) else -1

