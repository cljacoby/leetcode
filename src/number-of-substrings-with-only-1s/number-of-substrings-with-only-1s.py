# https://leetcode.com/problems/number-of-substrings-with-only-1s

# win = []
# win [1]
# win [1, 1]
# win [1, 1, 1]

class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr = 0 
        tot = 0
        for i in s:
            i = int(i)
            if i == 1:
                curr += 1
                tot += curr
            else:
                curr = 0
        tot = tot % (pow(10, 9) + 7)
        return tot

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("0110111", 9),
        ("101", 2),
        ("111111", 21),
    ]
    for (s, solution) in tests:
        result = sol.numSub(s)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

