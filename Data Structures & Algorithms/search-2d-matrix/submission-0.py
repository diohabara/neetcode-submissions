class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        # めぐる式の基本: 「okは条件を満たす」「ngは条件を満たさない」を先に決める
        # 今回は 2Dを1Dに見て、index k(0..m*n-1) の値が target以上になる最小kを探す(lower_bound)
        # 条件 P(k): matrix[k//m][k%m] >= target
        # okはP(ok)=Trueにできるよう、必ず条件を満たす番兵を用意したいが
        # 最大要素でもtarget未満の可能性があるので、okを「配列外」(m*n)にして番兵にする
        # ただし ok=m*n のときは実データ参照しないように P(k) を実装する
        def P(k: int) -> bool:
            # kが範囲外なら「条件を満たす(番兵)」として扱う
            # これで ok=m*n は常にTrue、ng=-1は常にFalseが作れる
            if m*n<=k:
                return True
            return target<=matrix[k//m][k%m]
        ng=-1 # P(ng)=False(配列外の左番兵)
        ok=m*n # P(ok)=True(配列外の右番兵)
        while 1<ok-ng:
            mid=(ng+ok)//2
            if P(mid):
                ok=mid
            else:
                ng=mid
        # okは「>=targetになる最小インデックス」
        # okが配列外なら存在しない
        if m*n<=ok:
            return False
        return matrix[ok//m][ok%m]==target
        # 時間計算量: O(log(m*n))
        # 空間計算量: O(1)
