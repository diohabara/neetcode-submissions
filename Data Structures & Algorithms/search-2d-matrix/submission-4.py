from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        ok = 0
        ng = m
        if target < matrix[0][0]:
            return False
        while 1 < abs(ok - ng):
            mid = (ok + ng) // 2
            if matrix[mid][0] <= target:
                ok = mid
            else:
                ng = mid
        row = ok
        ok = -1
        ng = n
        while 1 < abs(ok - ng):
            mid = (ok + ng) // 2
            if matrix[row][mid] <= target:
                ok = mid
            else:
                ng = mid
        return ok != -1 and matrix[row][ok] == target