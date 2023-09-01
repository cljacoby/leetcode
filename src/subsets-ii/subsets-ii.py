# https://leetcode.com/problems/subsets

'''
Key Insights:
    - We can use a simple comparison of this index vs. last index
      instead of using a set. Additional notes in comments above each
      solution.
'''

# This way uses a set in each stack frame to avoid doing duplicate
# combination generations. I.e. if this value is in the `seen` set, we
# should skip it. This was the more obvious/intuitive way I first saw to
# solve the problem.
class _Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.solutions = [[]]
        path = list()
        nums = sorted(nums)
        self.step(nums, 0, path)
        return self.solutions

    def step(self, nums, pre, path):
        seen = set()
        for i, n in enumerate(nums[pre:]):
            if n in seen:
                continue
            seen.add(n)
            path.append(n)
            self.solutions.append(path[:])
            self.step(nums, pre+i+1, path)
            path.pop()

# Effectively same solution as above, but with memory-saving
# optimization avoiding allocation a set in each stack frame. Intead, we
# just compare the value of the current iteration with the value from
# the last iteration. If they're equivalent than we skip. This works
# because the input array was sorted at the beginning, so all duplicates
# will be located adajently.
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.solutions = [[]]
        path = list()
        nums = sorted(nums)
        self.step(nums, 0, path)
        return self.solutions

    def step(self, nums, pre, path):
        for i, n in enumerate(nums[pre:]):
            if i > 0 and nums[pre+i] == nums[pre+i-1]:
                continue
            path.append(n)
            self.solutions.append(path[:])
            self.step(nums, pre+i+1, path)
            path.pop()

def set_of_tuples(arr):
    return set([tuple(i) for i in arr])

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [1,2,2],
            [[],[1],[1,2],[1,2,2],[2],[2,2]],
        ),
        (
            [4,4,4,1,4],
            [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]],
        ),
    ]
    for (nums, solution) in tests:
        result = sol.subsetsWithDup(nums)
        s = set_of_tuples(solution)
        r = set_of_tuples(result)
        print(f"result = {result}, solution = {solution}")
        assert r == s, \
            f"result {r} != solution {s}"
    print("✅ All tests passed")


