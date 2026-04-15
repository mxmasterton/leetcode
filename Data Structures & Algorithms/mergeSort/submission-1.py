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
        self.mergeSortHelper(pairs, start_pointer, middle)
        self.mergeSortHelper(pairs, middle + 1, end_pointer)

        self.merge(pairs, start_pointer, end_pointer, middle)

        return pairs

    def merge(self, pairs, start_pointer, end_pointer, middle):
        left = pairs[start_pointer : middle + 1]
        right = pairs[middle + 1 : end_pointer + 1]

        left_pointer = 0
        right_pointer = 0
        result_pointer = start_pointer

        while left_pointer < len(left) and right_pointer < len(right):
            if left[left_pointer].key <= right[right_pointer].key:
                pairs[result_pointer] = left[left_pointer]
                left_pointer += 1
            else:
                pairs[result_pointer] = right[right_pointer]
                right_pointer += 1
            result_pointer += 1

        while left_pointer < len(left):
            pairs[result_pointer] = left[left_pointer]
            left_pointer += 1
            result_pointer += 1

        while right_pointer < len(right):
            pairs[result_pointer] = right[right_pointer]
            right_pointer += 1
            result_pointer += 1

        