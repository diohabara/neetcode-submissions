class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)
        while i < n:
            j = i # `#`まで読む
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1 # `j`から`length`文字が本体
            res.append(s[j: j+length])
            i = j + length # `j + length`は別の文字のprefix
        return res