# https://leetcode.com/problems/combination-sum-ii

'''
Notes:
    - I solved this more-or-less exactly equal to combination-sum, exact
      changing the handling of the `pre` index to not re-use candidates
    - I initially did not account for duplicates, and it took a couple
      tries to get it right. I initially sorted the index, thinking that
      would automatically take care of it, which it did not. I then
      changed the datatype of solutions from a list to a dict, and
      created a key as `hash(bytes(path))` to manage duplicate path
      values. However, this failed with a Time Limit Exceeded error,
      implying there was a way to trim out recursion paths
    - I then got the desired path of keeping a set of `seen` values at
      each stack frame. This solves the problem, and meets the runtime
      complexity requiremenets
    - Not sure if this would be a pass or fail, I guess would depend on
      how well it appeared I could debug the problem, and if I was just
      guessing between iterations, or actively thinking towards the
      correct solution.
    - Submitted it to claude for feedback and it pointed out that
      because candidates is sorted, I don't need to use a set per stack
      frame, instead I can just compare to the previous index, with the
      additional constraint that the comparison is only evaluated after
      the first iteration. I knew sorting had something to do with
      preventing duplicates, but missed on putting it all together.
    - Claude also suggested a pruning optimization. Given we're sorting
      candidates, if we see that a given candidates[i] > target - curr,
      we can skip trying any of the larger values
'''

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solutions = []
        candidates.sort()
        self.step(0, [], 0, solutions, candidates, target)
        return solutions
        
    def step(self, start, path, curr, solutions, candidates, target):
        if curr == target:
            solutions.append(path.copy())
            return
        if curr > target:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            # pruning: because candidates is sorted, if we see a
            # candidate exceeds the remaining balance to reach target,
            # we can break
            if candidates[i] > target - curr:
                break
            path.append(candidates[i])
            self.step(i + 1, path, curr + candidates[i], solutions, candidates, target)
            path.pop()
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [10, 1, 2, 7, 6, 1, 5],
            8,
            [
                [1, 1, 6],
                [1, 2, 5],
                [1, 7],
                [2, 6],
            ],
        ),
        (
            [2, 5, 2, 1, 2],
            5,
            [
                [1, 2, 2],
                [5],
            ],
        ),
        (
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            30,
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            ]

        )
    ]
    for (candidates, target, solution) in tests:
        result = sol.combinationSum2(candidates, target)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

