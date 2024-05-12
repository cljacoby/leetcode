# https://leetcode.com/problems/largest-local-values-in-a-matrix

# Simple brute force
class Solution(object):
    def maxLocal(self, x, y, grid):
        mx = -1
        gx, gy = x + 1, y + 1
        for i in range(gx - 1, gx + 2):
            for j in range(gy - 1, gy + 2):
                mx = max(mx, grid[i][j])
        return mx

    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(grid) - 2
        cols = len(grid[0]) - 2
        out = [[-1] * cols for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                out[i][j] = self.maxLocal(i, j, grid)
        return out


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [
                [9, 9, 8, 1],
                [5, 6, 2, 6],
                [8, 2, 6, 4],
                [6, 2, 2, 2]
            ],
            [[9, 9], [8, 6]]
        ),
        (
            [
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 2, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
            ],
            [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
        ),
    ]
    for (grid, solution) in tests:
        result = sol.largestLocal(grid)
        assert solution == result, \
            f"result {result} != solution {solution}, grid = {grid}"
    print("✅ All tests passed")
