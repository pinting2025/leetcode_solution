class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        if sum(candies) == k:
            return 1
        
        left = 1
        right = max(candies)
        ans = 0

        def is_valid(num):
            count = 0
            for i in range(len(candies)):
                if candies[i] < num:
                    continue
                elif candies[i] == num:
                    count += 1
                else:
                    split = candies[i] // num
                    count += split
            if count < k:
                return False
            return True

        while left <= right:
            mid = (left + right) // 2

            if is_valid(mid):
                left = mid + 1
                if mid > ans:
                    ans = mid
            else:
                right = mid - 1
        return ans


        