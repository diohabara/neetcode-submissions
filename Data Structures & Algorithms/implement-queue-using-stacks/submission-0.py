class MyQueue:
    # 直感: queueはfrontから取りたいが、stackはtopしか触れない
    # だからfrontを常に "どこかのtop" に置く
    # in: 新規pushを受ける(ここではtopがback)
    # out: pop/peek用(ここではtopがfront)
    # outが空のときだけ、inの要素をpopしてoutにpushし続けると順序が反転してfrontがtopに来る
    # 各要素はin->outへ高々1回しか移動しないので償却O(1)
    # time: push O(1), pop amortized O(1), peek amortized O(1), empty O(1)
    # space: O(N)
    def __init__(self):
        self.ins=[]
        self.out=[]
    def _move(self)->None:
        # outが空なら、inを全部outへ移す
        # これで最古の要素がoutのtopに来る
        if not self.out:
            while self.ins:
                self.out.append(self.ins.pop())
    def push(self,x:int)->None:
        # backに追加するだけ
        self.ins.append(x)
    def pop(self)->int:
        # frontがoutのtopに来るように必要なときだけ移す
        self._move()
        return self.out.pop()
    def peek(self)->int:
        self._move()
        return self.out[-1]
    def empty(self)->bool:
        return (not self.ins) and (not self.out)
