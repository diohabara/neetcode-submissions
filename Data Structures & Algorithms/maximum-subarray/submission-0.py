class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # current = 今の位置で終わる subarray の最大和
        current = nums[0]

        # best = 全体で見つかった最大和
        best = nums[0]

        for n in nums[1:]:
            # 今の n を前の subarray に足すか、
            # n から新しく始めるかを選ぶ
            current = max(current + n, n)

            # 全体の最大値を更新
            best = max(best, current)

        return best