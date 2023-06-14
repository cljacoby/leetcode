# https://leetcode.com/problems/house-robber

import json

# General algorithm structure implemented here; however, implemented by
# passing slices of the original nums. This makes for easier syntax, and
# easier grasping of the problem, but also means we can't cache results.
# Need to re-write by passing offset into nums instead of direct slice,
# and then cache on (offset, index) in each iteration of the `for` loop.
class _Solution1(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.step(nums, 0)

    def step(self, nums, tot):
        length = len(nums)
        m = tot
        for i, num in enumerate(nums):
            if i + 2 <= length:
                out = self.step(nums[i+2:], tot + num)
                m = max(m, out)
            else:
                m = max(m, tot + num)
        return m

# Argument structure revised to use index offset instead of direct
# slice. Caching not yet added.
class _Solution2(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.step(nums, len(nums), 0)

    def step(self, nums, length, pre):
        m = 0
        for i in range(pre, length):
            n = nums[i]
            if i + 2 <= length:
                n = n + self.step(nums, length, i + 2) 
            m = max(m, n)
        return m

# Full solution. Recursion using index offset instead of direct slice,
# and with caching of intermediate results.
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.step(nums, len(nums), 0, dict())

    def step(self, nums, length, pre, cache):
        m = 0
        for i in range(pre, length):
            n = nums[i]
            if i + 2 <= length:
                if (pre, i) in cache:
                    n = n + cache[(pre, i)]
                else:
                    cache[(pre, i)] = self.step(nums, length, i + 2, cache) 
                    n = n + cache[(pre, i)]
            m = max(m, n)
        return m




if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,2,3,1], 4),
        ([2,7,9,3,1], 12),
        ([2,1,1,2], 4),
        ([], 0),
        (json.load(open("test1.json")), 3365),
    ]
    for (nums, solution) in tests:
        print("*************************")
        result = sol.rob(nums)
        print(f"nums={nums}, result = {result}, solution = {solution}")
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

