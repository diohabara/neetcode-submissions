class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0,1,10,11,100,101,110,111
        # 1000,1001,1010,1011,1100,1101,1110,1111
        # 0, 1
        # 1, 2
        # 1, 2, 2, 3
        # 1, 2, 2, 3, 2, 3, 3, 4
        res = []
        # 0b1y = 
        for num in range(n+1):
            one = 0
            for i in range(32):
                if num & (1 << i):
                    one += 1
            res.append(one)
        return res