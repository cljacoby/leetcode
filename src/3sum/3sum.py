# https://leetcode.com/problems/3sum

import json

# First try. I think a valid solution, but exceeds time limit.
class _Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.solutions = set()
        for i in range(len(nums)):
            self.step(nums, i, list())
        out = [list(i) for i in self.solutions]
        return out

    def step(self, nums, index, path):
        length = len(nums)
        if index >= length:
            return
        path.append(nums[index])
        if len(path) == 3:
            if sum(path) == 0:
                self.solutions.add(tuple(sorted(path[:])))
        else:
            for i in range(index+1, length):
                self.step(nums, i, path)
        path.pop()
        return

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.solutions = set()
        self.nums = sorted(nums)
        # self.nums = nums
        self.length = len(self.nums)
        self.step(-1, list())
        out = [list(i) for i in self.solutions]
        return out

    def step(self, index, path):
        path_len = len(path)
        if path_len == 3:
            if sum(path) == 0:
                self.solutions.add(tuple(path))
            return
        elif (
            path_len == 2
            or path_len == 0
            or path_len == 1
        ):
            for i in range(index+1, self.length):
                path.append(self.nums[i])
                self.step(i, path)
                path.pop()
        else:
            assert False, "Unreachable"
'''
            try:
                diff = -1 * (path[0] + path[1])
                j = self.nums[index+1:].index(diff)
                self.solutions.add((path[0], path[1], self.nums[j]))
            except ValueError:
                pass
            return
'''
        


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [-1,0,1,2,-1,-4],
            [[-1,-1,2],[-1,0,1]],
        ),
        (
            [0,1,1],
            [],
        ),
        (
            [0,0,0],
            [[0,0,0]],
        ),
        (
            json.load(open("test1.json")),
            [],
        ),
    ]
    for (nums, solution) in tests:
        print("*************************")
        result = sol.threeSum(nums)
        solution = set([tuple(i) for i in solution])
        result = set([tuple(i) for i in result])
        print(f"nums = {nums}")
        print(f"result = {result}")
        print(f"solution = {solution}")
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

