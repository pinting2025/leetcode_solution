class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        
        def lcm(a: int, b: int) -> int:
            return a // gcd(a, b) * b

        res = []
        res.append(nums[0])
        
        for n in nums[1:]:
            # if gcd > 1, get lcm
            while res and gcd(n, res[-1]) > 1:
                n = lcm(n, res.pop())
            res.append(n)
        
        return res








        