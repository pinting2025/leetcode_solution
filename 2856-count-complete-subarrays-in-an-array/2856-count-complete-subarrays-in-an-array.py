class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target = len(set(nums))
        cur = set()
        res = 0
        
        for i in range(len(nums)):
            cur = set()

            for r in range(i, len(nums)):
                cur.add(nums[r])
                if len(cur) == target:
                    res += 1

        return res

            

        