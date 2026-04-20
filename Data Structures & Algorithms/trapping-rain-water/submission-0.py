class Solution:
    def trap(self, heights: List[int]) -> int:
        pre_min = 0
        post_min = 0
        prefix = [0] * len(heights)
        postfix = [0] * len(heights)
        for i in range(len(heights)):
            prefix[i] = pre_min
            pre_min = max(pre_min, heights[i])

            postfix[len(heights) - i - 1] = post_min
            post_min = max(post_min, heights[len(heights) - i - 1])

        total = 0
        for i in range(len(heights)):
            value = min(prefix[i], postfix[i]) - heights[i]
            if value > 0:
                total += value

        return total
