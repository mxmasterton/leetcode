class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(row, column):
            if (
                row == -1 or
                column == -1 or
                row == rows or
                column == columns or
                grid[row][column] == 0 or
                (row, column) in visited
            ):
                return 0

            visited.add((row, column))
            count = 1
            count += dfs(row - 1, column)
            count += dfs(row + 1, column)
            count += dfs(row, column - 1)
            count += dfs(row, column + 1)
            return count

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1 and (row, column) not in visited:
                    area = dfs(row, column)
                    max_area = max(max_area, area)

        return max_area