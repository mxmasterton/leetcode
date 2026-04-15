# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.mergeSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def mergeSortHelper(self, pairs, start_pointer, end_pointer):
        if end_pointer - start_pointer <= 0:
            return pairs

        middle = (start_pointer + end_pointer) // 2
        # start_pointer + (end_pointer - start_pointer) // 2 (overflow safe)

        self.mergeSortHelper(pairs, start_pointer, middle)
        self.mergeSortHelper(pairs, middle + 1, end_pointer)

        self.merge(pairs, start_pointer, middle, end_pointer)

        return pairs

    def merge(self, pairs, start_pointer, middle, end_pointer):
        left_half = pairs[start_pointer : middle + 1]
        right_half = pairs[middle + 1 : end_pointer + 1]

        left_pointer = 0
        right_pointer = 0
        result_pointer = start_pointer

        while left_pointer < len(left_half) and right_pointer < len(right_half):
            if left_half[left_pointer].key <= right_half[right_pointer].key:
                pairs[result_pointer] = left_half[left_pointer]
                left_pointer += 1
            else:
                pairs[result_pointer] = right_half[right_pointer]
                right_pointer += 1
            result_pointer += 1

        while left_pointer < len(left_half):
            pairs[result_pointer] = left_half[left_pointer]
            left_pointer += 1
            result_pointer += 1

        while right_pointer < len(right_half):
            pairs[result_pointer] = right_half[right_pointer]
            right_pointer += 1
            result_pointer += 1

        return pairs

        