class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n:
                correct = nums[i] - 1
                if nums[correct] == nums[i]:
                    break
                nums[i], nums[correct] = nums[correct], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
