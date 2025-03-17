class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        dic = Counter()
        ans = 1
        nums = set(nums)

        for i in nums:
            if i - 1 in dic:
                dic[i] = dic[i-1] + 1

            elif i - 1 in nums:
                n = 1
                c = 1
                while i - n in nums:
                    c += 1
                    n += 1
                dic[i] = c

            ans = max(ans, dic[i])
        
        return ans

