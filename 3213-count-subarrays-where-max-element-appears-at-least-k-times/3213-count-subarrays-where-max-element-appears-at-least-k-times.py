class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        cur = 0
        target = max(nums)
        res = 0

        for i in range(len(nums)):
            if nums[i] == target:
                cur += 1

            while cur >= k:
                res += (len(nums) - i)

                if nums[left] == target:
                    cur -= 1
                
                left += 1
        
        return res



            


            
