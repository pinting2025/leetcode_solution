class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        dec = [0] * (len(nums)+1)

        for start, end in queries:
            dec[start] += 1
            dec[end+1] -= 1
        
        minus = 0
        for i in range(len(nums)):
            minus += dec[i]
            if nums[i] > minus:
                return False
        return True
        
        # for q in queries:
        #     for i in range(q[0], q[1]+1):
        #         nums[i] -= 1
        
        # return max(nums) <= 0
