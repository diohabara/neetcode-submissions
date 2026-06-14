class Solution:
    def findClosestElements(self, arr, k, x):
        l=0
        r=len(arr)-1
        # 区間arr[l:r+1]を縮めて、長さがkになるまで続ける
        while k<r-l+1:
            # 左が右より近い(または同距離)なら右を捨てる
            # 同距離なら小さい方を残したいので右を捨てる(<=で右を縮める)
            if abs(x-arr[l])<=abs(x-arr[r]):
                r-=1
            else:
                l+=1
        return arr[l:r+1]
