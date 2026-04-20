class Solution:
    def checkInclusion(self, string_a: str, string_b: str) -> bool:
        if len(string_b) < len(string_a):
            return False

        count_a = [0] * 26
        count_b = [0] * 26

        for i in range(len(string_a)):
            count_a[ord(string_a[i]) - ord('a')] += 1
            count_b[ord(string_b[i]) - ord('a')] += 1

        if count_a == count_b:
            return True
        
        left_pointer = 0
        right_pointer = len(string_a) - 1

        while right_pointer < len(string_b) - 1:
            count_b[ord(string_b[left_pointer]) - ord('a')] -= 1
            left_pointer += 1

            right_pointer += 1
            count_b[ord(string_b[right_pointer]) - ord('a')] += 1

            if count_a == count_b:
                return True

        return False
            