class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count the number
        # return count is more than half
        c = Counter(nums)
        l = len(nums)
        for num, count in c.items():
            if l // 2 < count:
                return num
        return -1