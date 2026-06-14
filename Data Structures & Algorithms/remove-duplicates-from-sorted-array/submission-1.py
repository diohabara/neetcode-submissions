class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        write = 1 # nums[:write] are unique
        for read in range(1, n):
            if nums[write-1] != nums[read]:
                nums[write] = nums[read]
                write += 1
        return write