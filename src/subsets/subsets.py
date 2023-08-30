# https://leetcode.com/problems/subsets

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.solutions = [[]]
        path = list()
        self.step(nums, 0, path)
        return self.solutions

    def step(self, nums, pre, path):
        for i, n in enumerate(nums[pre:]):
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
            [1,2,3],
            [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]],
        ),
        (
            [0],
            [[], [0]]
        ),
    ]
    for (nums, solution) in tests:
        result = sol.subsets(nums)
        s = set_of_tuples(solution)
        r = set_of_tuples(result)
        assert r == s, \
            f"result {r} != solution {s}"
    print("✅ All tests passed")

