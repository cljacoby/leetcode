# https://leetcode.com/problems/combination-sum

# First solution. Passes acceptance, but pretty slow.
class _Solution(object):
    def combinationSum(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.combos = set()
        self.step(nums, target, list(), 0)
        return [list(i) for i in self.combos] 

    def step(self, nums, target, path, tot):
        for i in enumerate(nums):
            path.append(i)
            new_tot = tot + i
            if new_tot < target:
                self.step(nums, target, path, new_tot)
            elif new_tot == target:
                self.combos.add(tuple(sorted(path.copy())))
            path.pop()

# Vastly improved speed. Key observation that at each recursion, you
# only need to pass in the slice of numbers from the current offset
# forward. This reduces the number of recursions, and means we won't
# encounter re-arrangements of the same numbers. This means we don't
# need to rely on a set to replace duplicates, and can easily use a
# list-of-lists.
# 
# As a minor ergonomic improvement, if you decrement down from target
# rather than up from zero, you can save 1 argument, and a couple add
# instructions.
#
# Passing offset rather than slices reduces memory usage.
class Solution(object):
    def combinationSum(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.combos = list()
        self.step(nums, target, 0, list())
        return self.combos

    def step(self, nums, target, pre, path):
        if target < 0:
            return
        elif target == 0:
            self.combos.append(path.copy())
            return
        for (i, num) in enumerate(nums[pre:]):
            path.append(num)
            self.step(nums, target - num, pre + i, path)
            path.pop()


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2,3,6,7], 7, [[2,2,3],[7]]),
        ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
    ]
    for (nums, target, solution) in tests:
        result = sol.combinationSum(nums, target)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

