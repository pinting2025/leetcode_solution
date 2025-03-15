class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        left = 0
        right = max(nums)

        def is_valid(mid):
            # check if can find at least k non-adjacent houses value <= mid
            c = 0
            i = 0
            while i < len(nums):
                if nums[i] <= mid:
                    c += 1
                    i += 2
                else:
                    i += 1
                
                if c >= k:
                    return True
            return False

        while left <= right:
            mid = (left+right) // 2
            check = is_valid(mid)

            if check:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
        