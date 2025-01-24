# https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y),
        }
        stack = []
        for token in tokens:
            # print(f"token={token}, stack={stack}, tokens={tokens}")
            if token in ops:
                f = ops[token]
                b = stack.pop()
                a = stack.pop()
                stack.append(f(a, b))
            else:
                stack.append(int(token))
        assert len(stack) == 1, \
            f"stack did not end with single result, stack={stack}"
        return stack[0]

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (["2","1","+","3","*"], 9),
        (["4","13","5","/","+"], 6),
        (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),
    ]
    for (tokens, solution) in tests:
        result = sol.evalRPN(tokens)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

