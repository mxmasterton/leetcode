class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in string:
            if char in close_to_open:
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False