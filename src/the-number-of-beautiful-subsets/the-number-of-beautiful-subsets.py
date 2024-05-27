# https://leetcode.com/problems/the-number-of-beautiful-subsets

# Initial solution.
class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.nums = sorted(nums)
        self.count = 0
        self.k = k
        self.step(0, list())
        return self.count

    def beautiful(self, path, num):
        for x in path:
            if abs(x - num) == self.k:
                return False
        return True

    def step(self, pre, path):
        for i, num in enumerate(self.nums[pre:]):
            if self.beautiful(path, num):
                self.count += 1
                path.append(num)
                self.step(pre + i + 1, path)
                path.pop()

# ---------------------------------------------------------------

# Solution after reviewing other solutions with varying degrees of
# optimization.

from collections import defaultdict

class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        idx = 0
        nums.sort()
        freq = defaultdict(int)
        return self.step(idx, nums, k, freq) - 1

    def step(self, idx, nums, k, freq):
        if idx == len(nums):
            return 1
        tot = self.step(idx + 1, nums, k, freq)
        x = nums[idx]
        if x - k not in freq:
            freq[x] += 1
            tot += self.step(idx + 1, nums, k, freq)
            freq[x] -= 1
            if freq[x] == 0:
                del freq[x]
        return tot

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2,4,6], 2, 4),
        ([1], 1, 1),
    ]
    for nums, k, solution in tests:
        result = sol.beautifulSubsets(nums, k)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

