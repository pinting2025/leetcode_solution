class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        max_length = 1
        
        for i in range(1, len(nums)):
            for n in range(left, i):
                if nums[n] & nums[i] != 0:
                    left = n + 1

            max_length = max(max_length, i - left + 1)
        
        return max_length

        # left = 0
        # bit_mask = 0
        # max_length = 0

        # for i in range(len(nums)):
        #     while nums[left]




        


        


        
        