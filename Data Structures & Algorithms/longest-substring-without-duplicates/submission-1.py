class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        if not string:
            return 0

        inside = set()
        inside.add(string[0])

        left_pointer = 0
        right_pointer = 0
        max_size = 1

        while right_pointer < len(string) - 1:
            right_pointer += 1
            while string[right_pointer] in inside:
                inside.remove(string[left_pointer])
                left_pointer += 1
            inside.add(string[right_pointer])
            max_size = max(max_size, right_pointer - left_pointer + 1)

        return max_size
                
        