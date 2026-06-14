class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        lr, rl = [1]*(l), [1]*(l)
        for i in range(l-1):
            lr[i+1] = lr[i] * nums[i]
        for i in range(l-2, -1, -1):
            rl[i] = rl[i+1] * nums[i+1]
        return [lr[i] * rl[i] for i in range(l)]