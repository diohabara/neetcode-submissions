from typing import List


class Solution:

    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        # 探索範囲を最小にし、j が負になるのを防ぐため短い方を nums1 にする
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # n, m: 各配列の長さ / tot: 全要素数 / half: 左半分に必要な要素数
        n, m = len(nums1), len(nums2)
        tot = n + m
        half = (tot + 1) // 2

        # is_ok(i): nums1 から i 個取ったとき、nums1の左端 <= nums2の右端 を満たすか
        # i が小さいほど l1 は小さく r2 は大きくなるため、単調性（True -> False）がある
        def is_ok(i: int) -> bool:
            j = half - i
            l1 = float("-inf") if i == 0 else nums1[i - 1]
            r2 = float("inf") if j == m else nums2[j]
            return l1 <= r2

        # ok: 必ず条件を満たす個数（0個なら l1 = -inf なので必ず True）
        # ng: 必ず条件を満たさない個数（n + 1個は範囲外なので必ず False）
        ok, ng = 0, n + 1

        # ループ不変条件: ok は常に条件を満たし、ng は常に条件を満たさない
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid

        # ループ終了時、ok が「l1 <= r2 を満たす最大の個数」＝正解の分割位置
        # （このときもう一方の条件 l2 <= r1 も自動的に満たされている）
        i = ok
        j = half - i

        # 境界の4値を取得（端の要素がない場合は無限大を番兵にして条件式を統一する）
        l1 = float("-inf") if i == 0 else nums1[i - 1]
        r1 = float("inf") if i == n else nums1[i]
        l2 = float("-inf") if j == 0 else nums2[j - 1]
        r2 = float("inf") if j == m else nums2[j]

        # 奇数個なら左半分の最大値が中央値、偶数個なら左の最大値と右の最小値の平均
        if tot % 2 == 1:
            return float(max(l1, l2))
        return (max(l1, l2) + min(r1, r2)) / 2.0