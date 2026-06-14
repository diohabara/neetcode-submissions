class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for c in cnt.values():
            if 1 < c:
                return True
        return False
