class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if 0 < i and a == nums[i - 1]: # a is not dup
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if 0 < three_sum:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res