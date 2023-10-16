# https://leetcode.com/problems/surrounded-regions

def pb(board):
    return "\n" + "\n".join([str(row) for row in board]) + "\n"

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.rows = len(self.board)
        self.cols = len(self.board[0])
        path = set()
        for i in range(self.rows):
            for j in range(self.cols):
                if self.step(i, j, path):
                    self.capture(path)
                path.clear()
        return self.board

    def capture(self, coords):
        for (i,j) in coords:
            self.board[i][j] = 'X'

    def step(self, x, y, path):
        if (
            x < 0
            or y < 0
            or x >= self.rows
            or y >= self.cols
        ):
            return False
        if (x,y) in path or self.board[x][y] == 'X':
            return True
        path.add((x,y))
        if (self.step(x + 1, y, path)
            and self.step(x - 1, y, path)
            and self.step(x, y + 1, path)
            and self.step(x, y - 1, path)
        ):
            return True
        return False


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [
                ["X","X","X","X"],
                ["X","O","O","X"],
                ["X","X","O","X"],
                ["X","O","X","X"]
            ],
            [
                ["X","X","X","X"],
                ["X","X","X","X"],
                ["X","X","X","X"],
                ["X","O","X","X"]
            ]
        ),
        (
            [
                ["O","O","O","O","X","X"],
                ["O","O","O","O","O","O"],
                ["O","X","O","X","O","O"],
                ["O","X","O","O","X","O"],
                ["O","X","O","X","O","O"],
                ["O","X","O","O","O","O"]
            ],
            [
                ["O","O","O","O","X","X"],
                ["O","O","O","O","O","O"],
                ["O","X","O","X","O","O"],
                ["O","X","O","O","X","O"],
                ["O","X","O","X","O","O"],
                ["O","X","O","O","O","O"]
            ]
        ),
        (
            [
                ["X","O","O","X","X","X","O","X","O","O"],
                ["X","O","X","X","X","X","X","X","X","X"],
                ["X","X","X","X","O","X","X","X","X","X"],
                ["X","O","X","X","X","O","X","X","X","O"],
                ["O","X","X","X","O","X","O","X","O","X"],
                ["X","X","O","X","X","O","O","X","X","X"],
                ["O","X","X","O","O","X","O","X","X","O"],
                ["O","X","X","X","X","X","O","X","X","X"],
                ["X","O","O","X","X","O","X","X","O","O"],
                ["X","X","X","O","O","X","O","X","X","O"]
            ],
            [
                ["X","O","O","X","X","X","O","X","O","O"],
                ["X","O","X","X","X","X","X","X","X","X"],
                ["X","X","X","X","X","X","X","X","X","X"],
                ["X","X","X","X","X","X","X","X","X","O"],
                ["O","X","X","X","X","X","X","X","X","X"],
                ["X","X","X","X","X","X","X","X","X","X"],
                ["O","X","X","X","X","X","X","X","X","O"],
                ["O","X","X","X","X","X","X","X","X","X"],
                ["X","X","X","X","X","X","X","X","O","O"],
                ["X","X","X","O","O","X","O","X","X","O"]
            ],
        ),
    ]
    for (board, solution) in tests:
        result = sol.solve(board)
        assert board == solution, \
            f"board {pb(board)} != solution {pb(solution)}"
    print("✅ All tests passed")

