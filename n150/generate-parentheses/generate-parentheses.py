# https://leetcode.com/problems/generate-parentheses

class Solution(object):
    def step(self, pre, opened, closed, n, solutions):
        if opened == n and closed == n:
            s = "".join(pre)
            solutions.append(s)
            return
        if opened > closed:
            pre.append(')')
            self.step(pre, opened, closed + 1, n, solutions)
            pre.pop()
        if opened < n:
            pre.append('(')
            self.step(pre, opened + 1, closed, n, solutions)
            pre.pop()

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        opened = 0
        closed = 0
        pre = []
        solutions = []
        self.step(pre, opened, closed, n, solutions)
        return solutions
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            3,
            ["((()))","(()())","(())()","()(())","()()()"],
        ),
        (
            1,
            ["()"],
        ),
    ]
    for (n, solution) in tests:
        result = sol.generateParenthesis(n)
        result = sorted(result)
        solution = sorted(solution)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

