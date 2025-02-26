# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray

class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = mx = mn = 0
        for x in nums:
            mx = max(x, mx + x)
            mn = min(x, mn + x)
            best = max(best, mx, abs(mn))
        return best



if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,-3,2,3,-4], 5),
        ([2,-5,1,-4,3,-2], 8),
    ]
    for (nums, solution) in tests:
        result = sol.maxAbsoluteSum(nums)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

