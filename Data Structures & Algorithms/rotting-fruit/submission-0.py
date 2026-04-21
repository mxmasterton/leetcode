class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        fresh = time = 0
        queue = deque()

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1:
                    fresh += 1
                if grid[row][column] == 2:
                    queue.append((row, column))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while fresh > 0 and queue:
            for i in range(len(queue)):
                row, column = queue.popleft()

                for dr, dc in directions:
                    new_row, new_column = row + dr, column + dc
                    if (
                        new_row in range(rows) and
                        new_column in range(columns) and
                        grid[new_row][new_column] == 1
                    ):
                        grid[new_row][new_column] = 2
                        queue.append((new_row, new_column))
                        fresh -= 1
            time += 1

        if fresh == 0:
            return time
        else:
            return -1