# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference

class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        num1 = 0
        num2 = 0
        for i in range(n + 1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        return num1 - num2


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (10, 3, 19),
        (5, 1, -15),
    ]
    for (n, m, solution) in tests:
        result = sol.differenceOfSums(n, m)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

