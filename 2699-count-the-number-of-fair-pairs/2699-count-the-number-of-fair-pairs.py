class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums = sorted(nums)
        res = 0

        def search(target, start_index, lower = True):
            left, right = start_index, len(nums) - 1

            if lower == True:
                while left <= right:
                    mid = (left+right) // 2
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
            else:
                while left <= right:
                    mid = (left+right) // 2
                    if nums[mid] <= target:
                        left = mid + 1
                    else:
                        right = mid - 1

            return left

        for i in range(len(nums)):
            left = search(lower - nums[i], i+1, lower = True)
            right = search(upper - nums[i], i+1, lower = False)
            res += (right-left)
            
        return res
