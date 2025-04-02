# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii

class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = [0] * n
        right = [0] * n
        for j in range(1, n):
            left[j] = max(left[j-1], nums[j-1])
            right[n - j - 1] = max(right[n - j], nums[n - j])
        mx = 0
        for j in range(1, n-1):
            mx = max(mx, (left[j] - nums[j]) * right[j])
        return mx
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([12,6,1,2,7], 77),
        ([1,10,3,4,19], 133),
    ]
    for (nums, solution) in tests:
        result = sol.maximumTripletValue(nums)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


