class Solution:
    def longestPalindrome(self, string: str) -> str:
        res_idx = 0
        res_length = 0

        for i in range(len(string)):
            # odd length
            left_pointer, right_pointer = i, i
            while left_pointer >= 0 and right_pointer < len(string) and string[left_pointer] == string[right_pointer]:
                if right_pointer - left_pointer + 1 > res_length:                
                    res_idx = left_pointer
                    res_length = right_pointer - left_pointer + 1
                left_pointer -= 1
                right_pointer += 1

            # even length
            left_pointer, right_pointer = i, i + 1
            while left_pointer >= 0 and right_pointer < len(string) and string[left_pointer] == string[right_pointer]:
                if (right_pointer - left_pointer + 1) > res_length:
                    res_idx = left_pointer
                    res_length = right_pointer - left_pointer + 1
                left_pointer -= 1
                right_pointer += 1

        return string[res_idx: res_idx + res_length]