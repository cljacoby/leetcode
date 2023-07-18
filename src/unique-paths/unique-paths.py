# https://leetcode.com/problems/unique-paths

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.i_min = 0
        self.j_min = 0
        self.i_max = m - 1
        self.j_max = n - 1
        self.cache = dict()
        return self.step(0, 0)

    def step(self, i, j):
        if (
            i < self.i_min
            or i > self.i_max
            or j < self.j_min
            or j > self.j_max
        ):
            return 0
        if i == self.i_max and j == self.j_max:
            return 1
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        a = self.step(i + 1, j)
        b = self.step(i, j + 1)
        self.cache[(i, j)] = a + b
        return self.cache[(i, j)]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (3, 2, 3),
        (3, 7, 28),
    ]
    for (m, n, solution) in tests:
        result = sol.uniquePaths(m, n)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")
