class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ng, ok = 0, max(piles) 
        while 1 < abs(ok - ng):
            mid = (ok + ng) // 2
            hours = sum((p+mid-1) // mid for p in piles)
            if hours <= h:
                ok = mid
            else:
                ng = mid
        return ok