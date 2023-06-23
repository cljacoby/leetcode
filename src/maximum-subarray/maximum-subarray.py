# https://leetcode.com/problems/maximum-subarray

import json

# First attempt. Fails due to exceeding memory limit. Also very slow on
# big test sets. O(N^2) time complexity.
class Solution1(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = dict()
        length = len(nums)
        m = -1 * pow(10, 5)
        
        for win in range(1, length + 1):
            for i in range(length):
                j = i + win
                if j > length:
                    break
                if (i, j-1) in memo:
                    # print("cache hit")
                    s = memo[(i,j)] = memo[(i, j-1)] + nums[j-1]
                else:
                    # print("cache miss")
                    s = memo[(i, j)] = sum(nums[i:j])
                m = max(s, m)
                # print(f"i={i}, j={j}, win={win}, nums[i:j]={nums[i:j]}, s={s}")
        return m

# Got this via a hint in solutions. Key observation is that if a given
# element N is greater than the current running sub-array, you can
# restart the running sub-array at N. This allows doing in a single
# O(N) pass.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        curr_sum = max_sum = nums[0]
        for n in nums[1:]:
            curr_sum = max(curr_sum + n, n)
            max_sum = max(curr_sum, max_sum)
        return max_sum

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),
        ([5,4,-1,7,8], 23),
        (json.load(open("test1.json")), 11081),
    ]
    for (nums, solution) in tests:
        result = sol.maxSubArray(nums)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

