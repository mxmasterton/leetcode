class Solution:
    def characterReplacement(self, string: str, k: int) -> int:
        counts = [0] * 26

        left_pointer = 0
        right_pointer = 0
        max_size = 1

        counts[ord(string[0]) - ord('A')] += 1

        while right_pointer < len(string) - 1:
            right_pointer += 1
            counts[ord(string[right_pointer]) - ord('A')] += 1
            while right_pointer - left_pointer + 1 - max(counts) > k:
                counts[ord(string[left_pointer]) - ord('A')] -= 1
                left_pointer += 1
                
            max_size = max(max_size, right_pointer - left_pointer + 1)

        return max_size
