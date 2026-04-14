class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [None] * (2 * n)

        for i, num in enumerate(nums):
            out[i] = out[n + i] = num

        return out