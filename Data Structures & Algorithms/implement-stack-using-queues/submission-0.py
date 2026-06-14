class MyStack:
    def __init__(self):
        self.q = deque()
        self.d = deque()
    def push(self, x: int) -> None:
        # 方針: qのfrontを常にstackのtopにする
        # 手順: 既存要素をdに退避→xをqへ→dをqへ戻す(結果としてxがfrontになる)
        while self.q:
            self.d.append(self.q.popleft())
        self.q.append(x)
        while self.d:
            self.q.append(self.d.popleft())
        # 時間計算量: O(n) 空間計算量: O(n)
    def pop(self) -> int:
        # qのfrontがtopなので、frontからpopするだけ
        # 注意: removeも必要なのでpopleftを使う
        return self.q.popleft()
        # 時間計算量: O(1) 空間計算量: O(1)
    def top(self) -> int:
        # Queue操作のpeek(front)として先頭を見る
        return self.q[0]
        # 時間計算量: O(1) 空間計算量: O(1)
    def empty(self) -> bool:
        # dequeの空判定を素直に使う
        return not self.q
        # 時間計算量: O(1) 空間計算量: O(1)