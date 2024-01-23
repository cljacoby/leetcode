# https://leetcode.com/problems/minimum-falling-path-sum


class Solution(object):
    DIRS = [-1, 0, 1]

    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.cache = dict()
        ret = float("inf")
        for j in range(self.cols):
            ret = min(self.step(0, j), ret)
        return ret

    def step(self, i, j):
        if (i >= self.rows
            or i < 0
            or j >= self.cols
            or j < 0
        ):
            return float("inf")
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        if i == self.rows - 1:
            return self.matrix[i][j]
        ret = float("inf")
        for dy in self.DIRS:
            x = i + 1
            y = j + dy
            ret = min(ret, self.step(x, y))
        ret += self.matrix[i][j]
        self.cache[(i, j)] = ret
        return ret


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[2, 1, 3], [6, 5, 4], [7, 8, 9]], 13),
        ([[-19, 57], [-40, -5]], -59),
        (
            [
                [100, -42, -46, -41],
                [31, 97, 10, -10],
                [-58, -51, 82, 89],
                [51, 81, 69, -51],
            ],
            -36,
        ),
    ]
    for (matrix, solution) in tests:
        result = sol.minFallingPathSum(matrix)
        assert result == solution, \
            f"result {result} == solution {solution}"
    print("✅ All tests passed")
