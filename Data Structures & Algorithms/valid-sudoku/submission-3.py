class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(9):
            seen = set()
            for j in range(9):
                entry = board[i][j]
                if entry != ".":
                    if entry in seen:
                        return False
                    seen.add(entry)


        # check cols
        for i in range(9):
            seen = set()
            for j in range(9):
                entry = board[j][i]
                if entry != ".":
                    if entry in seen:
                        return False
                    seen.add(entry)

        # check squares
        for i in range(9):
            i1 = i // 3
            i2 = i % 3

            seen = set()
            for j in range(9):
                j1 = j // 3
                j2 = j % 3

                entry = board[3 * i1 + j1][3 * i2 + j2]
                if entry != ".":
                    if entry in seen:
                        return False
                    seen.add(entry)

        return True