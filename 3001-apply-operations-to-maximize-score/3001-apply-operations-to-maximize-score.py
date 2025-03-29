# class Solution:
#     def maximumScore(self, nums: List[int], k: int) -> int:
#         # get prime list
#         max_num = max(nums)
#         is_prime = [True] * (max_num + 1)
#         is_prime[0] = is_prime[1] = False
        
#         for i in range(2, int(max_num ** 0.5) + 1):
#             if is_prime[i]:
#                 for j in range(i*i, max_num + 1, i):
#                     is_prime[j] = False

#         # get prime count
#         score = {}
#         if num == 1:
#             score.add()
#         count = 0
#         if num in is_prime:
#             count += 1
#         for i in range(2, int(sqrt(num))+1):
#             if num % i == 0:
#                 if i in is_prime:
#                     count += 1
#                 if num // i != i and num // i in is_prime:
#                     count += 1

#         # # get prime list
#         # max_num = max(nums)
#         # is_prime = set(range(2, max_num+1))
        
#         # for n in range(2, int(sqrt(max_num))+1):
#         #     if n in is_prime:
#         #         m = set(range(n*n, max_num+1, n))
#         #         is_prime -= m

#         # def prime_count(num):
#         #     if num == 1:
#         #         return 0
#         #     count = 0
#         #     if num in is_prime:
#         #         count += 1
#         #     for i in range(2, int(sqrt(num))+1):
#         #         if num % i == 0:
#         #             if i in is_prime:
#         #                 count += 1
#         #             if num // i != i and num // i in is_prime:
#         #                 count += 1
#         #     return max(1, count)

#         # # calculate prime score
#         # score = []
#         # for n in nums:
#         #     score.append(prime_count(n))
        
#         # # hint 2
#         # n = len(nums)
#         # left = [-1] * n
#         # right = [n] * n
#         # for i in range(0, n):
#         #     # find left most
#         #     move = 1
#         #     while i - move >= 0:
#         #         if score[i-move] >= score[i]:
#         #             left[i] = i - move
#         #             break
#         #         move += 1

#         #     # find right most
#         #     move = 1
#         #     while i + move < len(nums):
#         #         if score[i+move] > score[i]:
#         #             right[i] = i + move
#         #             break
#         #         move += 1
                
#         # # hint 4
#         # ranges = []
#         # for i in range(n):
#         #     valid_left = i - left[i]
#         #     valid_right = right[i] - i
#         #     ranges.append(valid_left * valid_right)

#         # # hint 5
#         # processed = [(i, score[i], nums[i]) for i in range(n)]
#         # processed = sorted(processed, key = lambda x: (-x[2], -x[1], x[0]))
#         # res = 1
#         # mod = 10**9 + 7
#         # for i, c, s in processed:
#         #     choose = min(ranges[i], k)
#         #     k -= choose
#         #     res = (res * s ** choose) % mod
#         #     # print(s, choose, ranges[i])

#         #     if k <= 0:
#         #         break
        
#         # return res % mod


import math
import heapq
from collections import defaultdict


class Solution:
    def maximumScore(self, nums, k):
        mod = 10**9 + 7
        n = len(nums)

        prime_scores = [0] * n
        memo = {}

        def calculate_prime_score(num):
            if num in memo:
                return memo[num]

            score = 0
            orig_num = num
            for factor in range(2, int(math.sqrt(num)) + 1):
                if num % factor == 0:
                    score += 1
                    while num % factor == 0:
                        num //= factor

            if num > 1:
                score += 1
            memo[orig_num] = score
            return score

        for i in range(n):
            prime_scores[i] = calculate_prime_score(nums[i])

        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        operations = []
        for i in range(n):
            count = (i - left[i]) * (right[i] - i)
            operations.append((-nums[i], count))

        operations.sort()
        result = 1
        for neg_val, count in operations:
            val = -neg_val
            ops = min(count, k)
            if ops > 0:
                result = (result * pow(val, ops, mod)) % mod
                k -= ops

            if k == 0:
                break
        return result