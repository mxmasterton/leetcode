class Solution:
    def isPalindrome(self, string: str) -> bool:
        left_pointer = 0
        right_pointer = len(string) - 1

        while left_pointer < right_pointer:
            while left_pointer < right_pointer and not string[left_pointer].isalnum():
                left_pointer += 1

            while left_pointer < right_pointer and not string[right_pointer].isalnum():
                right_pointer -= 1   

            if string[left_pointer].lower() != string[right_pointer].lower():
                return False

            left_pointer += 1
            right_pointer -= 1 
            
        return True