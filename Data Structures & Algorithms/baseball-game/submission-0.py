class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for token in operations:
            match token:
                case "+":
                    stack.append(stack[-1] + stack[-2])
                case "D":
                    stack.append(stack[-1] * 2)
                case "C":
                    stack.pop()
                case _:
                    stack.append(int(token))

        return sum(stack)