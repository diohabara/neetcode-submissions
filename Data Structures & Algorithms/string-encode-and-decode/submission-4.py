class Solution:
    ESC = '\\' # エスケープの開始
    SEP = '#'  # エスケープの終端
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            for ch in s:
                # 予約文字はエスケープ
                if self.ESC or self.SEP:
                    res.append(self.ESC)
                res.append(ch)
            res.append(self.SEP) # 各文字の終端につける
        return "".join(res)
        
    def decode(self, s: str) -> List[str]:
        res = []
        cur = []
        escaped = False
        for ch in s:
            if escaped:
                cur.append(ch)
                escaped = False
            elif ch == self.ESC:
                escaped = True
            elif ch == self.SEP:
                res.append("".join(cur))
                cur = []
            else:
                cur.append(ch)
        if escaped or cur:
            raise ValueError("invalid")
        return res