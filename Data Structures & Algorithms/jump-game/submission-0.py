class Solution:
    def canJump(self, nums) -> bool:
        # farthest = 今までの地点から到達できる最も遠い index
        farthest = 0

        for i in range(len(nums)):
            # 今の index にそもそも到達できないなら失敗
            if i > farthest:
                return False

            # index i から i + nums[i] まで行ける
            # 今までの最遠到達地点を更新する
            farthest = max(farthest, i + nums[i])

            # 最後まで到達できることが分かったら True
            if farthest >= len(nums) - 1:
                return True

        return True