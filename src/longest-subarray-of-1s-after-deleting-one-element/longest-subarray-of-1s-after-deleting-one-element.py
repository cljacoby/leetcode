# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element

from collections import deque

# Solution using double ended queue.
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        window = deque()
        mx = -1
        zcount = 0
        for num in nums:
            window.append(num)
            if num == 0:
                zcount += 1
                while zcount > 1 and len(window) > 0:
                    if window.popleft() == 0:
                        zcount -= 1
            mx = max(mx, len(window))
        return mx - 1

# Solution using 2 pointers.
# Interestingly this solution runs slower in Leetcode than the previous.
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = right = zcount = 0
        mx = -1
        for i in range(len(nums)):
            right += 1
            if nums[i] == 0:
                zcount += 1
                while zcount > 1 and right - left > 0:
                    if nums[left] == 0:
                        zcount -= 1
                    left += 1
            mx = max(mx, right - left)
        return mx - 1


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([0,1,1,1,0,1,1,0,1], 5),
    ]
    for (nums, solution) in tests:
        result = sol.longestSubarray(nums)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

