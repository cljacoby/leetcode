# https://leetcode.com/problems/jump-game

import json

# Top-down DFS with memoization. Programmatically correct, but
# still exceeds time limit.
class Solution1(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.cache = dict()
        self.nums = nums
        self.last = len(self.nums) - 1
        return self._step(0)

    def _step(self, index):
        # print(f"index={index}, n={self.nums[index]}")
        if index in self.cache:
            return self.cache[index]
        if index > self.last:
            return False
        if index == self.last:
            return True
        n = self.nums[index]
        if n == 0:
            return False
        ret = False
        for i in range(index + 1, min(index + n, self.last) + 1):
            if self._step(i):
                ret = True
                break
        self.cache[index] = ret
        return self.cache[index]

# This was kind of one of those "one-sweet-trick" leetcode problems,
# where basically you either pick up one one secret trick to solve the
# problem, or else no other solutions work. 
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dest = len(nums) - 1
        for i in range(dest, -1, -1):
            # GreaterThanOrEqual because you can jump up to nums[i]
            # steps, not just nums[i] distance exclusively
            if i + nums[i] >= dest:
                dest = i
        return dest == 0


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2,3,1,1,4], True),
        ([3,2,1,0,4], False),
        ([2,0], True),
        (json.load(open("test1.json")), True),
        (json.load(open("test2.json")), False),
    ]
    for (i, (nums, solution)) in enumerate(tests):
        result = sol.canJump(nums)
        assert result == solution, \
            f"result {result} != solution {solution}, test case {i}"
    print("✅ All tests passed")

