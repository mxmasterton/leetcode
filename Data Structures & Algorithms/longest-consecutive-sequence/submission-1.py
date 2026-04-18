class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_length = 0
        for num in num_set:
            if num - 1 not in num_set:
                max_length = max(max_length, 1)
            else:
                current = num
                while current + 1 in num_set:
                    current += 1
                max_length = max(current - num + 2, max_length)

        return max_length
                

