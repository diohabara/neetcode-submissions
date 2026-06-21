class Solution:
    def reverseBits(self, n: int) -> int:
        tmp = ["0"] * 32
        i = 0
        while n:
            if n & 1:
                tmp[-(i+1)] = "1"
            i += 1
            n >>= 1
        return int("".join(reversed(tmp)), base=2)