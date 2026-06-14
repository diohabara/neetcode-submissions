class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        res = []
        i = 0
        while i < n:
            if 0 < i and nums[i] == nums[i - 1]:
                i += 1
                continue
            if i + 3 < n:
                min_sum = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
                if target < min_sum:
                    break
                max_sum = nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3]
                if max_sum < target:
                    i += 1
                    continue
            j = i + 1
            while j < n:
                if i + 1 < j and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                if j + 2 < n:
                    min_sum = nums[i] + nums[j] + nums[j + 1] + nums[j + 2]
                    if target < min_sum:
                        break
                    max_sum = nums[i] + nums[j] + nums[n - 1] + nums[n - 2]
                    if max_sum < target:
                        j += 1
                        continue
                k = j + 1
                l = n - 1
                while k < l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        l -= 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif s < target:
                        k += 1
                    else:
                        l -= 1
                j += 1
            i += 1
        return res
