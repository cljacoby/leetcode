# https://leetcode.com/problems/generate-parentheses

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        buf = []
        solutions = []
        self.step(buf, solutions, n, n)
        return solutions

    def step(self, buf, solutions, n_open, n_close):
        if n_close == 0:
            solutions.append("".join(buf))
            return
        if n_open > 0:
            buf.append("(")
            self.step(buf, solutions, n_open - 1, n_close)
            buf.pop()
        if n_open < n_close:
            buf.append(")")
            self.step(buf, solutions, n_open, n_close - 1)
            buf.pop()
        
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (3, ["((()))","(()())","(())()","()(())","()()()"]),
        (1, ["()"]),
    ]
    for (n, solution) in tests:
        result = sol.generateParenthesis(n)
        assert set(result) == set(solution), \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

