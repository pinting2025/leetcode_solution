class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                cur = nums[left] + nums[right] + nums[i]
                if cur == 0:
                    temp = tuple(sorted([nums[left], nums[right], nums[i]]))
                    if temp not in res:
                        res.add(temp)
                    left += 1
                    right -= 1
                
                else:
                    if cur < 0:
                        left += 1
                    else:
                        right -= 1
        
        return list(res)
