# https://leetcode.com/problems/combination-sum

'''
Notes:
    - Straight forward intuition of generating combinatons with
      repitition.
    - Caught myself on some small bugs, i.e. self check, not a failed
      submission:
        - Initially did `self.step(pre + i, ...)` when the prefix was
          already factored in by doing `range(pre, len(candidates))`
        - I initially did `solutions.append(path)`, and got a list of
          empty lists when I ran locally. I realized the problem was
          python's reference vs value semantics, and needed to copy the
          `path` list when adding to the `solutions` list.

'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solutions = []
        self.step(0, 0, [], candidates, target, solutions)
        return solutions

    def step(self, pre, curr, path, candidates, target, solutions):
        if curr == target:
            solutions.append(path.copy())
            return
        elif curr > target:
            return
        for i in range(pre, len(candidates)):
            path.append(candidates[i])
            self.step(i, curr + candidates[i], path, candidates, target, solutions)
            path.pop()

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2,3,6,7], 7, [[2,2,3],[7]]),
        ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
        ([2], 1, []),
    ]
    for (candidates, target, solution) in tests:
        result = sol.combinationSum(candidates, target)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

