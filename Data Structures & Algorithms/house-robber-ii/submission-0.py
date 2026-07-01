class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_line(houses: List[int]) -> int:
            prev2 = 0
            prev1 = 0
            for n in houses:
                current = max(prev1, prev2+n)
                prev2 = prev1
                prev1 = current
            return prev1
        return max(
            rob_line(nums[1:]),
            rob_line(nums[:-1])
        )