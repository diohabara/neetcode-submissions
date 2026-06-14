class MyHashSet:
    def __init__(self):
        self.a = bytearray((1_000_001 + 7) // 8)

    def add(self, key: int) -> None:
        self.a[key >> 3] |= 1 << (key & 7)

    def remove(self, key: int) -> None:
        self.a[key >> 3] &= ~(1 << (key & 7))

    def contains(self, key: int) -> bool:
        return (self.a[key >> 3] >> (key & 7)) & 1 == 1
