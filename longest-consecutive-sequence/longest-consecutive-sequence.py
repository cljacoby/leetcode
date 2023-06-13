# https://leetcode.com/problems/longest-consecutive-sequence

import json

# First attempt. I believe O(n^2) complexity.
class _Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for n in nums:
            s.add(n)
        peak = 0
        for n in nums:
            i = n
            while i in s:
                i += 1
            peak = max(peak, i - n)
        return peak

# Using sort. Technically violates problem constraints due to O(n*logn)
# complexity of the sort; however, was accepted solution.
class _Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        nums.sort()
        peak = streak = 1
        last = pow(10, 9) + 1
        for i in nums:
            if i == last + 1:
                streak += 1
                peak = max(streak, peak)
            elif i == last:
                continue
            else:
                streak = 1
            last = i
        return peak

# Initial solution was actually very close to the ideal solution. The
# key observations are:
#  1. After creating the set, and iterating back over the numbers, you
#     should be removing observed numbers from the set as you go. You
#     don't need to repeat, as if its still in the set is not part of any
#     already observed sequence.
#   2. In order for point 1 to work correctly without a sorted input,
#      when performing the iteration over the set members, you should
#      increment both up and down to find all current set entries in
#      sequence
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        s = set(nums)
        peak = streak = 1
        while len(s) > 0:
            i = s.pop()
            streak = 1
            j = i + 1
            while j in s:
                streak += 1
                s.remove(j)
                j += 1
            j = i - 1
            while j in s:
                streak += 1
                s.remove(j)
                j -= 1
            peak = max(streak, peak)
        return peak
            
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([100,4,200,1,3,2], 4),
        ([1,2,0,1], 3),
        ([0,3,7,2,5,8,4,6,0,1], 9),
        (json.load(open("test1.json")), 100000),
    ]
    for (nums, solution) in tests:
        result = sol.longestConsecutive(nums)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

