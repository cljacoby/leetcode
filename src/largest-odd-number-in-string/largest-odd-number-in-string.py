# https://leetcode.com/problems/largest-odd-number-in-string

class Solution(object):
    def largestOddNumber(self, s):
        """
        :type num: str
        :rtype: str
        """
        for i in reversed(range(len(s))):
            x = int(s[i])
            if x != 0 and x % 2 != 0:
                return s[0:i+1]
        return ""

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("52", "5"),
        ("4206", ""),
        ("35427", "35427"),
    ]
    for (s, solution) in tests:
        result = sol.largestOddNumber(s)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

