# https://leetcode.com/problems/permutations

'''
Notes:
    - SolutionB was the one I wrote first. Its the way I intuitively
      solve the problem; however, all the array slicing should generate
      a bunch of data copying. I wrote SolutionA as a "no-copy"
      alternative, in the sense we only use the single copy of the
      original nums while doing the permutation logic (obviously there's still
      copying when appending to `solutions`). Ironically, according to
      Leetcode SolutionA produced a higher memory footprint. It could be
      the fact that the memory for `solutions` dominates, and/or noise of
      the Leetcode platform runtime itself.
    - In SolutionA, we're basically popping elements out of the remaining
      numbers and appending to the growing permutation as an equivalent of doing
      `nums[:i] + nums[i+1:]`
'''

from collections import deque

class SolutionA(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.solutions = []
        rem = deque(nums)
        self.step([], rem)
        return self.solutions
        
    def step(self, perm, rem):
        n = len(rem)
        if n == 0:
            self.solutions.append(perm.copy())
        for i in range(n):
            nxt = rem.popleft()
            perm.append(nxt)
            self.step(perm, rem)
            perm.pop()
            rem.append(nxt)


class SolutionB(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.solutions = []
        self.n = len(nums)
        self.step([], nums) 
        return self.solutions

    def step(self, perm, nums):
        if len(perm) == self.n:
            assert len(nums) == 0, "perm is full, but nums not exhausted"
            self.solutions.append(perm.copy())
            return
        for i in range(len(nums)):
            perm.append(nums[i])
            self.step(perm, nums[:i] + nums[i+1:])
            perm.pop()



if __name__ == "__main__":
    for Solution in [SolutionA, SolutionB]:
        sol = Solution()
        tests = [
            (
                [1,2,3],
                [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]],
            ),
            (
                [0,1],
                [[0,1],[1,0]],
            ),
            (
                 [1],
                 [[1]],
            )
        ]
        for (nums, solution) in tests:
            result = sol.permute(nums)
            result.sort()
            solution.sort()
            assert result == solution, \
                f"result {result} != solution {solution}"
        print("✅ All tests passed")

