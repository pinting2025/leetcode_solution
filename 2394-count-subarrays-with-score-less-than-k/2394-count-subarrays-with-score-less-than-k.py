class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Prefix array construction
        pre = []
        for num in nums:
            if not pre: 
                pre.append(num)
            else: 
                pre.append(pre[-1] + num)

        # Binary Search helper function
        def helper(start, end):
            val = pre[end] - pre[start] + nums[start]
            count = end - start + 1
            return count * val < k
        
        # Looping to get the end for every index
        res = 0
        n = len(nums)
        for idx, num in enumerate(nums):
            left, right = idx, n - 1
            while left <= right:
                mid = (left + right) // 2
                if helper(idx, mid):
                    left = mid + 1
                else:
                    right = mid - 1
            res += (right - idx) + 1
        return res