class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums)*2)
        n = len(nums)
        for i in range(2):
            for j in range(n):
                ans[i*n + j] = nums[j]
        return ans