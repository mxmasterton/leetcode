class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = -1

        left_pointer = 0
        right_pointer = len(heights) - 1
        while left_pointer <= right_pointer:
            area = min(heights[left_pointer], heights[right_pointer]) * (right_pointer - left_pointer)
            max_area = max(area, max_area)

            if heights[left_pointer] < heights[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area