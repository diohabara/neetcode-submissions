from heapq import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        heap = [(-n, i) for i, n in enumerate(nums[:k])]
        heapify(heap)
        res = [-heap[0][0]]
        for i in range(k, n):
            heappush(heap, (-nums[i], i))
            while heap[0][1] <= i-k:
                heappop(heap)
            res.append(-heap[0][0])
        return res