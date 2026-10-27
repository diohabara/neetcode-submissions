class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        acc = nums[0]
        for i in range(1, n):
            res[i] *= acc
            acc *= nums[i]
        acc = nums[-1]
        for i in range(n-2,-1,-1):
            res[i] *= acc
            acc *= nums[i]
        return res