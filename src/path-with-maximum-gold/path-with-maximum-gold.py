# https://leetcode.com/problems/path-with-maximum-gold

class Solution(object):
    DIRS = [
        (1, 0),  # down
        (0, 1),  # right
        (-1, 0), # left
        (0, -1), # up
    ]

    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.path = set()
        mx = 0
        for i in range(self.rows):
            for j in range(self.cols):
                mx = max(mx, self.step(i, j))
        return mx

    def step(self, x, y):
        if (x < 0
            or y < 0
            or x >= self.rows
            or y >= self.cols
            or self.grid[x][y] == 0
            or (x, y) in self.path
        ):
            return 0
        self.path.add((x, y))
        mx = 0
        for (dx, dy) in self.DIRS:
            mx = max(mx, self.step(x + dx, y + dy))
        self.path.remove((x, y))
        return self.grid[x][y] + mx

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [
                [0,6,0],
                [5,8,7],
                [0,9,0]
            ],
            24,
        ),
        (
            [
                [1,0,7],
                [2,0,6],
                [3,4,5],
                [0,3,0],
                [9,0,20]
            ],
            28,
        )
    ]
    for (grid, solution) in tests:
        result = sol.getMaximumGold(grid)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

