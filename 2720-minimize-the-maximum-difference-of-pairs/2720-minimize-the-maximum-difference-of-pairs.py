class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
            
        nums = sorted(nums)

        l = 0
        r = abs(nums[-1] - nums[0])

        def helper(target):
            temp = []
            count = p
            flag = False
            for i in range(0, len(nums)-1):
                if flag == True:
                    flag = False
                    continue

                if abs(nums[i] - nums[i+1]) <= target:
                    count -= 1
                    flag = True

                elif temp and abs(nums[i] - temp[-1]) <= target:
                    count -= 1
                    temp.pop()
                else:
                    temp.append(nums[i])

                if count == 0:
                    return True

            return False
                     

        while l <= r:
            mid = (l+r) // 2
            if helper(mid):
                r = mid - 1
            else:
                l = mid + 1
            
        return l