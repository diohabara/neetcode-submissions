class MinStack:

    def __init__(self):
        self.stack = []

    # get 
    def push(self, val: int) -> None:
        min_val = min(self.getMin(), val)
        self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return 2**32
        return self.stack[-1][1]