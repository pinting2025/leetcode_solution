class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count_nums = Counter(nums)
        max_count = max(count_nums.values())
        res = 0

        for num, count in count_nums.items():
            if count == max_count:
                res += count
            
        return res

        


