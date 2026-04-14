# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left_pointer = 1
        right_pointer = n

        while left_pointer <= right_pointer:
            middle = (left_pointer + right_pointer) // 2

            if guess(middle) == -1:
                right_pointer = middle - 1
            elif guess(middle) == 1:
                left_pointer = middle + 1
            else:
                return middle
        