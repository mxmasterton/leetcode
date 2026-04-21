class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        cache = [[-1] * columns for _ in range(rows)]

        def dfs(row, column):
            if (
                row == rows or
                column == columns or
                grid[row][column] == 1
            ):
                return 0
            if row == rows - 1 and column == columns - 1:
                return 1
            if cache[row][column] > -1:
                return cache[row][column]

            cache[row][column] = dfs(row + 1, column) + dfs(row, column + 1)
            return cache[row][column]

        return dfs(0, 0)