class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10 ** 9 + 7
        num_odd = 0
        num_even = 0
        nums = [0] * 10
        N = len(nums)
        
        for index, x in enumerate(num):
            nums[int(x)] += 1
            if index % 2 == 1:
                num_odd += 1
            else:
                num_even += 1

        @cache 
        def calc(index, odd_left, even_left, s):
            if index == N:
                return int(s == 0)
            
            total = 0
            
            left_amt = nums[index]
            right_amt = 0
            while left_amt >= 0:          
                if left_amt <= odd_left and right_amt <= even_left:
                    diff = left_amt - right_amt
                    
                    total += calc(index + 1, odd_left - left_amt, even_left - right_amt, s + diff * index) * math.comb(odd_left, left_amt) * math.comb(even_left, right_amt)
                    total %= MOD
                left_amt -= 1
                right_amt += 1
            return total % MOD
        return calc(0, num_odd, num_even, 0)


        # nums = [int(d) for d in num]
        
        # if sum(nums) % 2 != 0:
        #     return 0
        
        # dic = Counter(nums)

        # memo = {}
        # target = sum(nums) // 2

        # def dp(i, even_sum, d_count):
        #     if (i, even_sum, d_count) in memo:
        #         return memo[(i, even_sum, d_count)]
            
        #     if d_count > len(num) or even_sum > target:
        #         return 0
            
        #     # if odd 
        #     if d_count % 2 == 0:
        #         even_sum += 

            

            








        

        