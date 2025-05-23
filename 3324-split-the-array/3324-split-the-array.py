class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        dic = Counter(nums)
        nums1 = 0
        nums2 = 0

        for val, count in dic.items():
            if count > 2:
                return False
            
            if count == 2:
                nums1 += 1
                nums2 += 1
            
            else:
                if nums1 >= nums2:
                    nums2 += 1
                else:
                    nums1 += 1
        
        return nums1 == nums2


       