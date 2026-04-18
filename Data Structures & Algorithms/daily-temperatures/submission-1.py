class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        
        stack = []
        out = [0] * len(temps)
        for i in range(len(temps) - 1, -1, -1):
            while stack and stack[-1][0] <= temps[i]:
                print(stack.pop())

            if not stack:
                out[i] = 0
            else:
                out[i] = stack[-1][1] - i
            stack.append([temps[i], i])

        return out

            