class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 直感: RPNは「数は積む」「演算子が来たら直近2つを確定できる」= LIFOが必要 => stack
        stack = []
        for t in tokens:
            if t != "+" and t != "-" and t != "*" and t != "/":
                stack.append(int(t))
                continue
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:
                # 仕様: 0方向への切り捨て(truncate toward zero)
                # Pythonの//は負数で床になるので不適
                stack.append(int(a / b))
        # valid RPNなら最後は1要素
        return stack[0]
# Time: O(n)
# Space: O(n)
