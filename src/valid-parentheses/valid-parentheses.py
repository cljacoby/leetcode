# https://leetcode.com/problems/valid-parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_open = set(['(', '[', '{'])
        s_close = set([')', ']', '}'])
        stack = list()
        for char in s:
            if char in s_open:
                stack.append(char)
            elif char in s_close:
                if len(stack) == 0:
                    return False
                op = stack.pop()
                if (
                    (char == ']' and op != '[')
                    or (char == ')' and op != '(')
                    or (char == '}' and op != '{')
                ):
                    return False
        if len(stack) > 0:
            return False
        return True

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
    ]
    for (s, solution) in tests:
        result = sol.isValid(s)
        assert solution == result, \
            f"result {result} != solution {solution}, test={s}"
    print("✅ All tests passed")

