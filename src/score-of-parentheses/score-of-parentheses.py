# https://leetcode.com/problems/score-of-parentheses

'''
Key Insight:
    - The problem clicked when I realized you need to initialize the
      stack with a baseline entry. Then when you finish iterating over
      the characters, the stack should have a final length of one,
      and the value is the answer
    - Before I was trying to use a `curr` variable to track intermediate
      values when inner parentheses pairs were completed. However the
      insight is basically this:
        
        stack[-1] += (1 if tmp == 0 else 2 * tmp)

      Or basically that you don't use any sort of `curr` / `tmp` variable,
      instead when you complete a parentheses pair, you update the value
      of the next stack frame
'''

class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        for ch in s:
            if ch == '(':
                stack.append(0)
            elif ch == ')':
                assert len(stack) > 1, "unbalanced input - too many close parens"
                tmp = stack.pop()
                stack[-1] += (1 if tmp == 0 else 2 * tmp)
            else:
                assert False, "illegal input char"
        assert len(stack) == 1, "unbalanced input - too many open parens"
        return stack[0]

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("()", 1),
        ("(())", 2),
        ("()()", 2),
        ("(()())", 4),
        ("((())(()))", 8),
    ]
    for (s, solution) in tests:
        result = sol.scoreOfParentheses(s)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

