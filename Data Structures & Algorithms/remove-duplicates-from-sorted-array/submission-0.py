class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        used = set()
        unique_cnt = 0
        for i in range(len(nums)):
            # if equal, last_num and unique_cnt unchanged
            # otherwise, increment the count and swap it with i and change last num
            if nums[i] not in used:
                nums[unique_cnt] = nums[i]
                unique_cnt += 1
                used.add(nums[i])
        return unique_cnt