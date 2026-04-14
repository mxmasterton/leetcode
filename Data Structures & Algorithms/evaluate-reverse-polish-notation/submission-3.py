class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        eval_stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = eval_stack.pop()
                a = eval_stack.pop()

                if token == "+":
                    eval_stack.append(a + b)
                elif token == "-":
                    eval_stack.append(a - b)
                elif token == "*":
                    eval_stack.append(a * b)
                else:
                    eval_stack.append(int(a / b))

            else:
                eval_stack.append(int(token))

        return eval_stack[-1]


        