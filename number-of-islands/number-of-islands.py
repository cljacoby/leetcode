# https://leetcode.com/problems/number-of-islands


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = grid
        self.islands = 0
        self.seen = [
            [False for j in range(len(self.grid[0]))] for i in range(len(self.grid))
        ]
        for i, row in enumerate(self.grid):
            for j, _cell in enumerate(row):
                if self._step(i, j) > 0:
                    self.islands += 1
        return self.islands

    def _step(self, i, j):
        if (
            i < 0
            or j < 0
            or i >= len(self.grid)
            or j >= len(self.grid[0])
            or self.grid[i][j] == "0"
            or self.seen[i][j]
        ):
            return 0
        self.seen[i][j] = True
        size = 1
        size += self._step(i + 1, j)
        size += self._step(i - 1, j)
        size += self._step(i, j + 1)
        size += self._step(i, j - 1)
        return size


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ],
            1
        ),
        (
            [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ],
            3
        ),
    ]
    for (i, (grid, solution)) in enumerate(tests):
        result = sol.numIslands(grid)
        assert result == solution, \
            f"test {i} | result {result} != solution {solution}"
    print("✅ All tests passed")
