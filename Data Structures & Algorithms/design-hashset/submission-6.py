class MyHashSet:
    def __init__(self):
        # (桁 x あまり)を使ってデータを保存する
        self.set = bytearray((1_000_000 + 0b111) // 0b1000)

    def add(self, key: int) -> None:
        # //8と同じ。keyを桁数に変換
        i = key >> 3
        # %8と同じ。keyを値に変換
        offset = key & 0b111
        # 一意にkeyを値に変換
        self.set[i] |= 1 << offset

    def remove(self, key: int) -> None:
        i = key >> 3
        offset = key & 0b111
        self.set[i] &= ~(1 << offset)

    def contains(self, key: int) -> bool:
        i = key >> 3
        offset = key & 0b111
        return ((self.set[i] >> offset) & 1) == 1
