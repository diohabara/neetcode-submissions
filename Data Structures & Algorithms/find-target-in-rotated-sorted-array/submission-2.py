class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # 直感: 毎回、左右どちらか半分は昇順に整列している=範囲判定で捨てられる
        # 時間計算量: O(log n)
        # 空間計算量: O(1)
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            # 左半分[low..mid]が昇順なら、ここは通常の二分探索と同じ範囲判定ができる
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            # 右半分[mid..high]が昇順
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1