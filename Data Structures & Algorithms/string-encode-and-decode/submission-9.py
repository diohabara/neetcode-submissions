class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        <num_of_str><sep><str>
        """
        res = []
        for s in strs:
            res.append(f"{len(s)};{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """
        1. read until `;`
        2. read n chars
        3. concat it into res
        """
        res = []
        ptr = 0
        n = len(s)
        while ptr < n:
            num = 0
            while s[ptr] != ";":
                num *= 10
                num += int(s[ptr])
                ptr += 1
            cur = s[ptr+1:ptr+1+num]
            ptr += 1 + num
            res.append("".join(cur))
        return res