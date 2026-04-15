# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, pairs, start_pointer, end_pointer):
        if end_pointer - start_pointer <= 0:
            return

        left_pointer = start_pointer
        for i in range(start_pointer, end_pointer):
            if pairs[i].key < pairs[end_pointer].key:
                pairs[i], pairs[left_pointer] = pairs[left_pointer], pairs[i]
                left_pointer += 1
        pairs[left_pointer], pairs[end_pointer] = pairs[end_pointer], pairs[left_pointer]

        self.quickSortHelper(pairs, start_pointer, left_pointer - 1)
        self.quickSortHelper(pairs, left_pointer + 1, end_pointer)