# https://leetcode.com/problems/backspace-string-compare

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = self.process(s)
        t = self.process(t)
        return s == t

    def process(self, string):
        stack = list()
        for char in string:
            if char == "#":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(char)
        return stack

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("ab#c",    "ad#c",     True),
        ("ab##",    "c#d#",     True),
        ("a#c",     "b",        False),
    ]
    for (s, t, solution) in tests:
        result = sol.backspaceCompare(s, t)
        assert result == solution, \
            "result {result} != solution {solution}"
    print("✅ All tests passed")

