# https://leetcode.com/problems/majority-element

from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = defaultdict(int)
        mx = (float('nan'), float('-inf'))
        for num in nums:
            counts[num] += 1
            if counts[num] > mx[1]:
                mx = (num, counts[num])
        return mx[0]

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2,2,1,1,1,2,2], 2),
        ([3,2,3], 3),
    ]
    for (nums, solution) in tests:
        result = sol.majorityElement(nums)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

