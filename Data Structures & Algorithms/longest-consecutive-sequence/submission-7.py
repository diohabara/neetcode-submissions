class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        used = set()
        res = 0
        """
        1. count the num from min to max in num_set
        2. if cur+1 in set -> loop; otherwise next num
        """
        for cur in nums:
            count = 1
            if cur in used:
                continue
            while cur+1 in num_set:
                used.add(cur+1)
                count += 1
                cur += 1
            res = max(res, count)
        return res