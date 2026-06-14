class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            # 同じ値を先頭にすると同じ triplet が繰り返し出るのでスキップ
            if 0 < i and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    # 同じ値の l をまとめて飛ばす(重複 triplet 防止)
                    lv = nums[l]
                    while l < r and nums[l] == lv:
                        l += 1

                    # 同じ値の r をまとめて飛ばす(重複 triplet 防止)
                    rv = nums[r]
                    while l < r and nums[r] == rv:
                        r -= 1

                elif s < 0:
                    # 和が小さいので l を右へ(和を増やす)
                    l += 1
                elif 0 < s:
                    # 和が大きいので r を左へ(和を減らす)
                    r -= 1

        return res
