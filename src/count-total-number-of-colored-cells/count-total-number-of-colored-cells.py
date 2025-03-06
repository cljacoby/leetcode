# https://leetcode.com/problems/count-total-number-of-colored-cells

class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        tot = 1
        for i in range(n):
            add = 4 * i
            tot += add
        return tot

class Solution2(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 1 + n * (n - 1) * 2

if __name__ == "__main__":
    sol = Solution()
    sol2 = Solution2()
    tests = [
        (1, 1),
        (2, 5),
        (4, 25),
    ]
    for (n, solution) in tests:
        result = sol.coloredCells(n)
        result2 = sol2.coloredCells(n)
        assert result == solution, \
            f"result {result} != solution {solution}"
        assert result2 == solution, \
            f"result2 {result2} != solution {solution}"
    print("✅ All tests passed")

