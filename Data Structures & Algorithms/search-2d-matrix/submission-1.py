class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        left_pointer = 0
        right_pointer = n * m - 1

        while left_pointer <= right_pointer:
            middle = (left_pointer + right_pointer) // 2
            i = middle // m
            j = middle % m

            if matrix[i][j] < target:
                left_pointer = middle + 1
            elif matrix[i][j] > target:
                right_pointer = middle - 1
            else:
                return True

        return False