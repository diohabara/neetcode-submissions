class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i, n in enumerate(nums):
            comp[target - n] = i
        for j, n in enumerate(nums):
            if n in comp and j != comp[n]:
                return [j, comp[n]]
        return [-1, -1]