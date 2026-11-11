class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_ok(i):
            # nums[i]とtargetが同じ山
            if (nums[i] < nums[0]) == (target < nums[0]):
                return nums[i] >= target
            return nums[i] < nums[0]
        ng, ok = -1, len(nums)
        while abs(ok - ng) > 1:
            mid = (ok+ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        if ok < len(nums) and nums[ok] == target:
            return ok
        return -1

