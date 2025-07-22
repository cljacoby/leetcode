# https://leetcode.com/problems/maximum-difference-between-increasing-elements

# Practice expressing recurrance relations:
'''
Recurrance:
    dp[j] = max(dp[j-1], nums[j] - curr_min)    ; if nums[j] > curr_min
            dp[j-1]                             ; otherwise
    curr_min = min(nums[j], curr_min)


Initialization:
    dp[0] = [-1]
    curr_min = nums[0]
'''

class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        mx = -1
        i = 0
        for j in range(1, n):
            if nums[j] < nums[i]:
                i = j
            elif nums[j] > nums[i]:
                mx = max(mx, nums[j] - nums[i])
        return mx

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([7,1,5,4], 4),
        ([9,4,3,2], -1),
        ([1,5,2,10], 9),
    ]
    for (nums, solution) in tests:
        result = sol.maximumDifference(nums)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

