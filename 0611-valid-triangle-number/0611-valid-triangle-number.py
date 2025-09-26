class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # two pointers
        res = 0
        nums.sort()

        # i will be the largest number
        for l in range(2, len(nums)):
            i, j = 0, l - 1
            
            while i < j:
                if nums[i] + nums[j] > nums[l]:
                    res += j - i
                    j -= 1
                else:
                    i += 1
            
        return res







        # backtrack
        # res = 0
        # nums.sort()

        # def backtrack(idx, end):
        #     nonlocal res

        #     for i in range(idx, end-1):
        #         # check how many numbers between i and k with a j between them
        #         j = i + 1
        #         while j < end and nums[i] + nums[j] <= nums[end]:
        #             j += 1
        #         if j < end:
        #             res += (end - j)
        #     return
        
        # for i in range(2, len(nums)):
        #     backtrack(0, i)

        # return res




        