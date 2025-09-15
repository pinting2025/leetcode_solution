class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        res = [0, 0]

        for num, count in freq.items():
            if count % 2 != 0:
                res[1] += 1
            res[0] += (count // 2)
        
        return res


