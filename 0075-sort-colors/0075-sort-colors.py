class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic = Counter(nums)
        idx = 0
        color = 0
        while color <= 2:
            for _ in range(dic[color]):
                nums[idx] = color
                idx += 1
            color += 1
    
                
        