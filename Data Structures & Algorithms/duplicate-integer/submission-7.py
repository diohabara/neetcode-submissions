class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for count in counter.values():
            if count > 1:
                return True
        return False