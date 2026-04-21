class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(row, column):
            if (
                row == -1 or
                column == -1 or
                row == rows or
                column == columns or
                grid[row][column] == "0" or
                (row, column) in visited
            ):
                return
            else:
                visited.add((row, column))
                dfs(row - 1, column)
                dfs(row + 1, column)
                dfs(row, column - 1)
                dfs(row, column + 1)

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands