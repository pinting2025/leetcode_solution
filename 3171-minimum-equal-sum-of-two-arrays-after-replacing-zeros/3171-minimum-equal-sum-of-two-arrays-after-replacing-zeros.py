class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        zero1 = nums1.count(0)
        zero2 = nums2.count(0)

        for n in nums1:
            if n == 0:
                sum1 += 1
            else:
                sum1 += n 
        
        for n in nums2:
            if n == 0:
                sum2 += 1
            else:
                sum2 += n
        
        if sum1 > sum2:
            return sum1 if zero2 > 0 else -1
        elif sum1 == sum2:
            return sum1
        else:
            return sum2 if zero1 > 0 else -1






        # zero1 = Counter(nums1)[0]
        # zero2 = Counter(nums2)[0]
        
        # def helper(target):
        #     s1 = sum(nums1)
        #     s2 = sum(nums2)
            
        #     if s2 > s1:
        #         if zero1 == 0:
        #             return False
        #         s2 += zero2
        #         if s2 - s1 - zero1 < 0 or s2 > target:
        #             return False
        #     elif s1 == s2:
        #         if (zero1 != 0 and zero2 == 0) or (zero1 == 0 and zero2 != 0):
        #             return False
        #     else:
        #         if zero2 == 0:
        #             return False
        #         s1 += zero1
        #         if s1 - s2 - zero2 < 0 or s1 > target:
        #             return False
            
        #     return True
        
        # left = 1
        # right = max(sum(nums1), sum(nums2)) + max(zero1, zero2)

        # while left <= right:
        #     mid = int((left+right) // 2)
        #     if helper(mid):
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        
        # return left if helper(left) else -1