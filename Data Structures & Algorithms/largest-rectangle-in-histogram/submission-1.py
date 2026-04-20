class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # pair: (index, height)

        for index, height in enumerate(heights):
            start_index = index
            while stack and stack[-1][1] > height:
                pop_index, pop_height = stack.pop()
                max_area = max(max_area, (index - pop_index) * pop_height)
                start_index = pop_index
            stack.append((start_index, height))

        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))

        return max_area