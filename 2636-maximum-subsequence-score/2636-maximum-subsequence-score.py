class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        combine = sorted(zip(nums2, nums1), reverse = True)
        
        heap = []
        res = 0

        sumn1 = 0
        for n2, n1 in combine:
            heapq.heappush(heap, n1)
            sumn1 += n1

            if len(heap) > k:
                sumn1 -= heapq.heappop(heap)
            if len(heap) == k:
                res = max(res, sumn1 * n2)
        
        return res
            




