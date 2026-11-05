class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        rem_to_index = defaultdict(int)
        for i, n in enumerate(numbers):
            rem_to_index[target-n] = i
        for i, n in enumerate(numbers):
            if n in rem_to_index and rem_to_index[n] != i:
                return [i+1, rem_to_index[n]+1]