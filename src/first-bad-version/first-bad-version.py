# https://leetcode.com/problems/first-bad-version

"""
This problem is basically just annoying scaffolding
around a binary search through an array. It's annoying
because the `isBadVersion(version)` is implemted on the
leetcode server side, so its harder to run/test locally.
"""

"""
Key Insights:
    - Don't need to create an array, because it's all just
      sequential integers from 1..N. So just pass values directly
      and don't index.
    - I'm still not that strong writing a binary search using indices
      rather than slices. I wrote a version with slices off the top of
      my head, but converting it to indices took some thinking. I should
      practice this.
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return False

# Hack to mock function implemented on leetcode server
def make_is_bad_ver_func(bad):
    return lambda v: v >= bad

class Solution(object):
    def bisect(self, i, j):
        if isBadVersion(i):
            return i
        if not isBadVersion(j):
            return float('inf')
        if j - i == 1:
            return j
        mid = (j - i) // 2 + i
        a = self.bisect(i, mid)
        b = self.bisect(mid, j)
        return min(a, b)

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.bisect(1, n)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (5, 4),
        (1, 1),
    ]
    for (n, solution) in tests:
        locals()["isBadVersion"] = make_is_bad_ver_func(solution)
        result = sol.firstBadVersion(n)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")
