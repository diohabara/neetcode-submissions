import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        # divide into smaller, bigger
        pivot = random.choice(nums)
        smaller = [e for e in nums if e < pivot]
        equals = [e for e in nums if e == pivot]
        bigger = [e for e in nums if pivot < e]
        if 1 < len(smaller):
            smaller = self.sortArray(smaller)
        if 1 < len(bigger):
            bigger = self.sortArray(bigger)
        # merge
        return smaller + equals + bigger