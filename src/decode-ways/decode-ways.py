# https://leetcode.com/problems/decode-ways

from string import ascii_uppercase

class Solution(object):

    MAP = {str(i+1): char for (i, char) in enumerate(ascii_uppercase)}

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.cache = dict()
        return self.step(s)

    def step(self, s):
        if s == "":
            return 1
        if s in self.cache:
            return self.cache[s]
        a = b = 0
        if len(s) >= 1 and s[:1] in self.MAP:
            a = self.step(s[1:])
        if len(s) >= 2 and s[:2] in self.MAP:
            b = self.step(s[2:])
        self.cache[s] = a + b
        return self.cache[s]
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("12", 2),
        ("226", 3),
        ("06", 0),
    ]
    for (s, solution) in tests:
        result = sol.numDecodings(s)
        assert result == solution, \
            f"s='{s}', result {result} != solution {solution}"
    print("✅ All tests passed")

