class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        res, left = 0, 0
        counter = Counter()
        pairs = 0
        for i in range(len(nums)):
            # Expanding right pointer
            if nums[i] in counter:
                pairs += counter[nums[i]]
            counter[nums[i]] += 1

            # Shrinking left pointer:
            while left <= i and pairs >= k:
                res += len(nums) - i
                counter[nums[left]] -= 1
                pairs -= counter[nums[left]]
                left += 1  

        return res