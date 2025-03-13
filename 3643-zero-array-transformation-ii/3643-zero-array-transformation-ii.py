class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        # create an array using all query by marking the start and end point
        def sweep(queries):
            up_down = [0] * (len(nums)+1)
            for q in queries:
                s = q[0]
                e = q[1] + 1
                up_down[s] += q[2]
                up_down[e] -= q[2]
            
            cur = 0
            for i in range(len(up_down)):
                cur += up_down[i]
                up_down[i] = cur
            
            return up_down
        
        def valid(up_down):
            # check if it's possible to get zero array
            for i,j in zip(nums, up_down[:len(nums)]):
                if i > j:
                    return False
            return True
        
        if len(set(nums)) == 1 and nums[0] == 0:
            return 0

        up_down = sweep(queries)
        if not valid(up_down):
            return -1
        
        # if is possible to get zero array, we use bunary search to get the min q
        left = 0
        right = len(queries)
        ans = float('inf')

        while left <= right:
            mid = (left+right) // 2
            cur_q = queries[:mid+1]
            up_down = sweep(cur_q)

            if valid(up_down):
                ans = min(ans,mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return ans + 1



        