class Solution:
    def uniquePaths(self, rows: int, columns: int) -> int:
        cache = [[0] * columns for _ in range(rows)]

        def dfs(row, column):
            if row == rows - 1 and column == columns - 1:
                return 1
            if row == rows or column == columns:
                return 0
            if cache[row][column] > 0:
                return cache[row][column]

            cache[row][column] = dfs(row + 1, column) + dfs(row, column + 1)
            return cache[row][column]

        return dfs(0, 0)
        