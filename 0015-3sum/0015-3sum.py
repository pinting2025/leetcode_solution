class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # dic = Counter(nums)
        # nums = sorted(nums)
        # ans = []

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         dic[nums[i]] -= 1
        #         dic[nums[j]] -= 1
                
        #         if (0 - (nums[i] + nums[j]) in nums[j+1:]) and dic[0 - (nums[i] + nums[j])] != 0:
        #             # temp = sorted([nums[i], nums[j], (0 - (nums[i] + nums[j]))])
        #             # if temp not in ans:
        #             ans.append([nums[i], nums[j], (0 - (nums[i] + nums[j]))])
                
        #         dic[nums[i]] += 1
        #         dic[nums[j]] += 1
        
        # return ans
        
        nums = sorted(nums)

        def two_sum(numbers, target):
            seen = set()
            pairs = []

            for j in range(len(numbers)):
                complement = target - numbers[j]
                if complement in seen:
                    # only add this pair if we haven't added the same pair before
                    if not pairs or pairs[-1] != [complement, numbers[j]]:
                        pairs.append([complement, numbers[j]])
                seen.add(numbers[j])
            return pairs
        
        ans_p = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            p = two_sum(nums[i+1:], 0 - nums[i])

            if p != []:
                for n1, n2 in p:
                    ans_p.append([nums[i], n1, n2])
        
        return ans_p

            

                    