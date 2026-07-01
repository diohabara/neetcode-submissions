class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        ans = nums[0]
        for n in nums[1:]:
            candidate = (
                n,
                max_prod * n,
                min_prod * n
            )
            max_prod = max(candidate)
            min_prod = min(candidate)
            ans = max(ans, max_prod)
        return ans