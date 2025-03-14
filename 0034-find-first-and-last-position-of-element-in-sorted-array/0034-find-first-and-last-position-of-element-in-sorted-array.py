class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = []
        start_pos = -1
        end_pos = -1

        if nums == []:
            return [start_pos, end_pos]

        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target:
                start_pos = mid
                end_pos = mid
                c = 1
                while mid + c < len(nums) and nums[mid + c] == target:
                    end_pos = mid + c
                    c += 1

                c = 1
                while mid - c >= 0 and nums[mid - c] == target:
                    start_pos = mid - c
                    c += 1
                break
                # return [start_pos, end_pos]

            if nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1
        
        return [start_pos, end_pos]


