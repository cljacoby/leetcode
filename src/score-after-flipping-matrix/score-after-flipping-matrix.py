# https://leetcode.com/problems/score-after-flipping-matrix

class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            if grid[i][0] == 0:
                self.flip_row(grid, cols, i)
        for j in range(cols):
            count = {0: 0, 1: 0}
            for i in range(rows):
                count[grid[i][j]] += 1
            if count[0] > count[1]:
                self.flip_col(grid, rows, j)
        return sum([self.bin_to_dec(row) for row in grid])

    def flip_row(self, grid, cols, i):
        for j in range(cols):
            grid[i][j] = 0 if grid[i][j] else 1

    def flip_col(self, grid, rows, j):
        for i in range(rows):
            grid[i][j] = 0 if grid[i][j] else 1

    def bin_to_dec(self, row):
        return sum([pow(2, pos) * bit for (pos, bit) in enumerate(reversed(row))])


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [
                [0,0,1,1],
                [1,0,1,0],
                [1,1,0,0],
            ],
            39
        ),
        (
            [[0]],
            1
        )
    ]
    for (grid, solution) in tests:
        result = sol.matrixScore(grid)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

