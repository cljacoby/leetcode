# https://leetcode.com/problems/climbing-stairs

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cache = dict()
        self.cache[1] = 1
        self.cache[2] = 2
        return self._step(n)

    def _step(self, n):
        if n in self.cache:
            return self.cache[n]
        a = self._step(n - 1)
        b = self._step(n - 2)
        c = a + b
        self.cache[n] = c
        return c

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (2, 2),
        (3, 3),
    ]
    for (n, solution) in tests:
        result = sol.climbStairs(n)
        print(f"n={n}, solution={solution}, result={result}")
        assert result == solution, \
                f"result={result} != solution={solution}"
    print("✅ All tests passed")

