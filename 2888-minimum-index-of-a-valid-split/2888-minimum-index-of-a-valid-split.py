class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        dominate = max(nums_count.items(), key=lambda x: x[1])
        dominate_num = dominate[0]
        dominate_count = dominate[1]
        count = 0

        for i in range(len(nums)):
            if nums[i] == dominate_num:
                count += 1
            if count > ((i+1)//2):
                if (dominate_count - count) > (len(nums) - i - 1) // 2:
                    return i
                else:
                    continue
        
        return -1







        # nums_count = Counter(nums)
        # dominate = max(nums_count)
        
        # left = 0
        # right = len(nums) - 1

        # def is_valid(target):
        #     left_c = max(Counter(nums[0:target]))
        #     left_r = max(Counter(nums[target:]))
        #     if left_c == left_r and left_r == dominate:
        #         return True
        #     return False

        # while left <= right:
        #     mid = (left+right) // 2
        #     if is_valid(nums[mid]):
        #         left = mid - 1
        #     else:
        #         right = mid + 1
        
        # return left



