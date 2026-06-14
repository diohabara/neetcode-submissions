import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            rest = target - n
            j = bisect.bisect_left(numbers, rest)
            if 0 <= j < len(numbers) and n + numbers[j] == target:
                return [i+1, j+1]
        